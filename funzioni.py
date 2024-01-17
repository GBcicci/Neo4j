from neo4j import GraphDatabase

# neo4j_uri = "neo4j+s://ac0433a0.databases.neo4j.io"
neo4j_uri = "neo4j+s://126e5e68.databases.neo4j.io"
neo4j_user = "neo4j"
# neo4j_password = "Puxj8A5JEz6zEwTowkvsZGxZIpIwtoH-XXB5q2ymGck"
neo4j_password = "ok1OvaNkJZwzpa5O_GcOgmIRJqZZkHUBkwoZUXdOsdw"


def attiva() -> GraphDatabase.driver:
    # funzione che apre la connessione
    driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
    return driver


def spegni(driver: GraphDatabase.driver) -> None:
    # funzione che chiude la connessione
    driver.close()


def ottieni_nodi(driver: GraphDatabase.driver) -> list or bool:
    # funzione che restituisce una lista con tutti i nodi presenti
    # restituisce falso se non trova nulla
    try:
        session = driver.session()
        result = session.run("MATCH (n) RETURN n")
        nodi = [record['n']['nome'] for record in result]
        session.close()
        return nodi
    except:
        return False


def ottieni_piste_difficolta(driver):
    query = """
    MATCH ()-[n:PISTA]->()
    RETURN n.nome, n.difficolta
    """
    out = []
    with driver.session() as session:
        result = session.run(query)
        for record in result:
            record = dict(record)
            out.append([record['n.nome'], record['n.difficolta']])
    return out if out else False


def ottieni_piste_aperte(driver):
    query = """
    MATCH ()-[p:PISTA]->()
    RETURN p.nome, p.aperto
    """
    out = []
    with driver.session() as session:
        result = session.run(query)
        for record in result:
            record = dict(record)
            print(record)
            if record['p.aperto'] == True:
                out.append(f'{record["p.nome"]}: aperta')
            else:
                out.append(f'{record["p.nome"]}: chiusa')

    return out if out else False


def ottieni_percorso_breve(partenza: str, arrivo: str, seggiovie: bool, driver: GraphDatabase.driver) -> list or bool:
    # funzione che trova il percorso più breve tra due punti
    # restituisce una lista di piste in ordine di percorso
    # restituisce falso se non trova nulla

    MATCH = ''
    if seggiovie:
        MATCH = 'MATCH path = (start:Limite_pista {nome: \'' + partenza + '\'})-[:PISTA|SEGGIOVIA_SALITA|SEGGIOVIA_DISCESA|SKILIFT*]->(end:Limite_pista {nome:\'' + arrivo + '\'}) '
    else:
        MATCH = 'MATCH path = (start:Limite_pista {nome: \'' + partenza + '\'})-[:PISTA|SEGGIOVIA_SALITA|SKILIFT*]->(end:Limite_pista {nome:\'' + arrivo + '\'}) '
    WHERE = 'WHERE ALL(rel in relationships(path) WHERE rel.aperto = true) '
    RETURN = 'RETURN path, REDUCE(s = 0, rel IN relationships(path) | s + rel.tempo) AS tempo_totale '
    ORDER_BY = 'ORDER BY tempo_totale '
    LIMIT = 'LIMIT 1'
    query = MATCH + WHERE + RETURN + ORDER_BY + LIMIT
    print(query)
    try:
        temp_session = driver.session()
        result = temp_session.run(query)
        result = result.single()
        temp_session.close()
        path = result["path"]
        out_nodi = [node["nome"] for node in path.nodes]
        out_archi = [rel["nome"] for rel in path.relationships]
        print(out_nodi)
        print(out_archi)
    except:
        return False
    return out_nodi, out_archi, result["tempo_totale"]


def ottieni_percorso_facile(partenza: str, arrivo: str, seggiovie: bool,
                            driver: GraphDatabase.driver) -> list and int or bool:
    # funzione che trova il percorso più facile tra due punti
    # restituisce una lista di piste in ordine di percorso
    # restituisce falso se non trova nulla
    MATCH = ''
    if seggiovie:
        MATCH = 'MATCH path = (start:Limite_pista {nome: \'' + partenza + '\'})-[:PISTA|SEGGIOVIA_SALITA|SEGGIOVIA_DISCESA|SKILIFT*]->(end:Limite_pista {nome:\'' + arrivo + '\'}) '
    else:
        MATCH = 'MATCH path = (start:Limite_pista {nome: \'' + partenza + '\'})-[:PISTA|SEGGIOVIA_SALITA|SKILIFT*]->(end:Limite_pista {nome:\'' + arrivo + '\'}) '
    WHERE = 'WHERE ALL(rel in relationships(path) WHERE rel.aperto = true) '
    RETURN = 'RETURN path, REDUCE(s = 0, rel IN relationships(path) | s + rel.difficolta) AS difficoltà_totale '
    ORDER_BY = 'ORDER BY difficoltà_totale '
    LIMIT = 'LIMIT 1'
    query = MATCH + WHERE + RETURN + ORDER_BY + LIMIT
    try:
        temp_session = driver.session()
        result = temp_session.run(query)
        result = result.single()
        temp_session.close()
        path = result["path"]
        out_nodi = [node["nome"] for node in path.nodes]
        out_archi = [rel["nome"] for rel in path.relationships]
        print(out_nodi)
        print(out_archi)
    except:
        return False
    return out_nodi, out_archi, result["difficoltà_totale"]

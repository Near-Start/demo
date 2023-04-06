# _*_ coding: utf-8 _*_
from py2neo import Graph


class Neo4jTool:
    graph = None

    def __init__(self):
        print("Initialize Neo4j tools...")

    def connect2neo4j(self):
        self.graph = Graph("http://localhost:7474", name="neo4j", password="12345678")

    # 关系查询整个知识图谱体系
    def match_all_node(self):
        sql = "MATCH (n1)-[r]->(n2) RETURN n1,type(r),n2 LIMIT 500"
        answer = self.graph.run(sql).data()
        return answer

    # 关系查询:实体1
    def findRelationByEntity1(self, entity1):
        sql = "MATCH (n1{name:\"" + str(entity1) + "\"})-[r]->(n2) RETURN n1,type(r),n2"
        answer = self.graph.run(sql).data()
        # if(answer is None):
        # 	answer = self.graph.run("MATCH (n1:{name:\""+entity1+"\"})- [r] -> (n2) RETURN n1,r,n2" ).data()
        return answer

    # 关系查询：实体2
    def findRelationByEntity2(self, entity2):
        sql = "MATCH (n1)- [r] -> (n2 {name:\"" + str(entity2) + "\"}) RETURN n1,type(r),n2"
        answer = self.graph.run(sql).data()
        # if(answer is None):
        # 	answer = self.graph.run("MATCH (n1)- [r] -> (n2:{name:\""+entity2+"\"}) RETURN n1,r,n2" ).data()
        return answer

    # 根据关系查找
    def findEntityByRelation(self, relation):
        sql = "MATCH (n1)- [r: " + str(relation) + "] -> (n2) RETURN n1,type(r),n2"
        answer = self.graph.run(sql).data()
        return answer

    # 根据entity1和关系查找
    def findRelationByEntiti1andRelation(self, entity1, relation):
        sql = "MATCH (n1 {name:\"" + str(entity1) + "\"})- [r: " + str(relation) + "] -> (n2) RETURN n1,type(r),n2"
        answer = self.graph.run(sql).data()
        # if(answer is None):
        #	answer = self.graph.run("MATCH (n1:name {title:\"" + entity1 + "\"})- [r:RELATION {type:\""+relation+"\"}] -> (n2) RETURN n1,r,n2" ).data()
        return answer

    # 根据entity2和关系查找
    def findRelationByEntiti2andRelation(self, entity2, relation):
        sql = "MATCH (n1)- [r:" + str(relation) + "] -> (n2 {name:\"" + str(entity2) + "\"}RETURN n1,type(r),n2"
        answer = self.graph.run(sql).data()
        # if(answer is None):
        #	answer = self.graph.run("MATCH (n1)- [r:RELATION {type:\""+relation+"\"}] -> (n2:name {name:\"" + entity2 + "\"}) RETURN n1,rel,n2" ).data()
        return answer

    # 根据实体1和实体2查找
    def findRelationByEntiti1andEntiti2(self, entity1, entity2):
        sql = "MATCH (n1{name:\"" + str(entity1) + "\"})- [r] -> (n2{name:\"" + str(
            entity2) + "\"}) RETURN n1,type(r),n2"
        answer = self.graph.run(sql).evaluate()
        return answer
        # sql = "match p=shortestpath((n{name:\"" + str(entity1) + "\"})-[r*]-(m{name:\"" + str(entity2) + "\"})) RETURN p"
        # sql = "MATCH p=allshortestPaths((n{name:\"" + str(entity1) + "\"})-[*]-(m{name:\"" + str(entity2) + "\"})) with *,relationships(p) as r return p,r"
        # answer = self.graph.run(sql).data()
        # relationDict = []
        # if (answer is not None):
        #     for x in answer:
        #         tmp = {}
        #         start_node = x['p'].start_node
        #         end_node = x['p'].end_node
        #         tmp['n1'] = start_node
        #         tmp['n2'] = end_node
        #         tmp['r'] = x['r']
        #         relationDict.append(tmp)
        # return relationDict

    # 根据实体1-关系-实体2查找
    def findEntityRelation(self, entity1, relation, entity2):
        sql = "MATCH (n1{name:\"" + str(entity1) + "\"})- [r:" + str(relation) + "] -> (n2{name:\"" + str(
            entity2) + "\"}) RETURN n1,type(r),n2"
        answer = self.graph.run(sql).data()
        return answer

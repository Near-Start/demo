import sys

from web.neo4j_models import Neo4jTool

sys.path.append("..")

neo_con = Neo4jTool()  # 预加载neo4j
neo_con.connect2neo4j()
print('Neo4j has connected...')

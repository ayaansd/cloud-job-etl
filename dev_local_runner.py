
import duckdb, os
DB = "etl.duckdb"
con = duckdb.connect(DB)
for f in sorted(os.listdir("sql/transformations")):
    if f.endswith(".sql"):
        sql = open(os.path.join("sql/transformations", f)).read()
        con.execute(sql)
print("Tables:", con.execute("show tables").fetchall())
print("Top companies:", con.execute("select * from agg_top_companies limit 10").fetchdf())

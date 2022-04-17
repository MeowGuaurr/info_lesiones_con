import os
import csv
import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    "postgresql://rjzhetzazvboor:9285dec06b6fd2250d94296b37b9e3d8fb84465c057cac3d2c9eab31c4341036@ec2-34-205-209-14.compute-1.amazonaws.com:5432/d6knp9md5h6bnu")
db = scoped_session(sessionmaker(bind=engine))

def main():
    file = open("extremidad_inferior.csv")
    reader_2 = csv.reader(file)
    for id, id_pais, nombre, afectado, porcentaje, total in reader_2:
        db.execute("INSERT INTO extremidad_inferior ( id, id_pais, nombre, afectado, porcentaje, total) VALUES (:id, :id_pais, :nombre, :afectado, :porcentaje, :total)",
                {"id":id, "id_pais":id_pais, "nombre":nombre, "afectado":afectado, "porcentaje":porcentaje, "total":total})
        print(
            f"Added in extremidad inferior table id:{id}, id_pais:{id_pais}, nombre:{nombre}")
        db.commit()

if __name__=="__main__":
    main()
import os
import csv
import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    "postgresql://rjzhetzazvboor:9285dec06b6fd2250d94296b37b9e3d8fb84465c057cac3d2c9eab31c4341036@ec2-34-205-209-14.compute-1.amazonaws.com:5432/d6knp9md5h6bnu")
db = scoped_session(sessionmaker(bind=engine))

def main():
    file_1 = open("cabezaytronco.csv")
    file_2 = open("extremidad_superior.csv")
    file_3 = open("extremidad_inferior.csv")
    file_4 = open("recomendaciones.csv")
    file_5 = open("referencia.csv")
    file_6 = open("evaluacion.csv")
    file_7 = open("lesion.csv")
    file_8 = open("tratamiento.csv")
    file_9 = open("enfermedad.csv")
    file_10 = open("sintomas.csv")
    file_11 = open("causas.csv")
    file_12 = open("pais.csv")
    reader_12 = csv.reader(file_12)
    for id_pais, nombre in reader_12:
        db.execute("INSERT INTO pais (id_pais, nombre) VALUES (:id_pais, :nombre)",
                {"id_pais":id_pais, "nombre":nombre})
        print(
                f"Added in pais table id_pais:{id_pais}, nombre:{nombre}")
        db.commit()
    reader_1 = csv.reader(file_1)
    for id, pais, nombre, afectado, porcentaje, total in reader_1:
        db.execute("INSERT INTO cabytronco ( id, pais, nombre, afectado, porcentaje, total) VALUES (:id, :pais, :nombre, :afectado, :porcentaje, :total)",
                {"id":id, "pais":pais, "nombre":nombre, "afectado":afectado, "porcentaje":porcentaje, "total":total})
        print(
            f"Added in cabeza y tronco table id:{id}, pais:{pais}, nombre:{nombre}")
        db.commit()

    reader_2 = csv.reader(file_2)
    for id, pais, nombre, afectado, porcentaje, total in reader_2:
        db.execute("INSERT INTO extremidad_superior ( id, pais, nombre, afectado, porcentaje, total) VALUES (:id, :pais, :nombre, :afectado, :porcentaje, :total)",
                {"id":id, "pais":pais, "nombre":nombre, "afectado":afectado, "porcentaje":porcentaje, "total":total})
        print(
            f"Added in extremidad superior table id:{id}, pais:{pais}, nombre:{nombre}")
        db.commit()

    reader_3 = csv.reader(file_3)
    for id, pais, nombre, afectado, porcentaje, total in reader_3:
        db.execute("INSERT INTO extremidad_inferior ( id, pais, nombre, afectado, porcentaje, total) VALUES (:id, :pais, :nombre, :afectado, :porcentaje, :total)",
                {"id":id, "pais":pais, "nombre":nombre, "afectado":afectado, "porcentaje":porcentaje, "total":total})
        print(
            f"Added in extremidad superior table id:{id}, pais:{pais}, nombre:{nombre}")
        db.commit()
    
    reader_4 = csv.reader(file_4)
    for recomendacion_id, pais, recomendacion, total, porcentaje in reader_4:
        db.execute("INSERT INTO recomendaciones ( recomendacion_id, pais, recomendacion, total, porcentaje) VALUES (:recomendacion_id, :pais, :recomendacion, :total, :porcentaje)",
                {"recomendacion_id": recomendacion_id, "pais":pais, "recomendacion":recomendacion, "total":total, "porcentaje":porcentaje})
        print(
            f"Added in recomendaciones table recomendacion_id:{recomendacion_id}, pais:{pais}, recomendacion:{recomendacion}")
        db.commit()
    
    reader_5 = csv.reader(file_5)
    for id_referencia, pais, referencia, total, porcentaje in reader_4:
        db.execute("INSERT INTO referencia ( id_referencia, pais, referencia, total, porcentaje) VALUES (:id_referencia, :pais, :referencia, :total, :porcentaje)",
                {"id_referencia":  id_referencia, "pais":pais, "referencia":referencia, "total":total, "porcentaje":porcentaje})
        print(
            f"Added in referencia table  id_referencia:{id_referencia}, pais:{pais}, referencia:{referencia}")
        db.commit()

    reader_6 = csv.reader(file_6)
    for id_evaluacion, pais, evaluacion, total, porcentaje in reader_6:
        db.execute("INSERT INTO evaluacion ( id_evaluacion, pais, evaluacion, total, porcentaje) VALUES (:id_evalucion, :pais, :evaluacion, :total, :porcentaje)",
                {"id_evaluacion": id_evaluacion, "pais":pais, "evaluacion":evaluacion, "total":total, "porcentaje":porcentaje})
        print(
            f"Added in evaluacion table id_evaluacion:{id_evaluacion}, pais:{pais}, evaluacion:{evaluacion}")
        db.commit()

    reader_7 = csv.reader(file_7)
    for id_lesion, pais, nombre, afectado, total, porcentaje in reader_7:
        db.execute("INSERT INTO lesion (id_lesion, pais, nombre, afectado, total, porcentaje) VALUES (:id_lesion, :pais, :nombre, :afectado, :total, :porcentaje)",
                {"id_lesion":id_lesion, "pais":pais, "nombre":nombre, "afectado":afectado, "total":total, "porcentaje":porcentaje})
        print(
            f"Added in lesion table id_lesion:{id_lesion}, pais:{pais}, nombre:{nombre}"
        )
        db.commit()
    
    reader_8 = csv.reader(file_8)
    for id_tratamiento, pais, nombre, afectado, total, porcentaje in reader_8:
        db.execute("INSERT INTO tratamiento (id_tratamiento, pais, nombre, afectado, total, porcentaje) VALUES (:id_tratamiento, :pais, :nombre, :afectado, :total, :porcentaje)",
                {"id_tratamiento":id_tratamiento, "pais":pais, "nombre":nombre, "afectado":afectado, "total":total, "porcentaje":porcentaje})
        print(
            f"Added in tratamiento table id_tratamiento:{id_tratamiento}, pais:{pais}, nombre:{nombre}"
        )
        db.commit()

    reader_9 = csv.reader(file_9)
    for id_enfermedad, pais, nombre, afectado, total, porcentaje in reader_9:
        db.execute("INSERT INTO enfermedad (id_enfermedad, pais, nombre, afectado, total, porcentaje) VALUES (:id_enfermedad, :pais, :nombre, :afectado, :total, :porcentaje)",
                {"id_enfermedad":id_enfermedad, "pais":pais, "nombre":nombre, "afectado":afectado, "total":total, "porcentaje":porcentaje})
        print(
            f"Added in enfermedad table id_enfermedad:{id_enfermedad}, pais:{pais}, nombre:{nombre}"
        )
        db.commit()
    
    reader_10 = csv.reader(file_10)
    for id_sintomas, pais, sintoma, afectado, total, porcentaje in reader_10:
        db.execute("INSERT INTO sintomas (id_enfermedad, pais, sintoma, afectado, total, porcentaje) VALUES (:id_enfermedad, :pais, :nombre, :afectado, :total, :porcentaje)",
                {"id_sintomas":id_sintomas, "pais":pais, "sintoma":sintoma, "afectado":afectado, "total":total, "porcentaje":porcentaje})
        print(
            f"Added in sintomas table id_sintomas:{id_sintomas}, pais:{pais}, sintoma:{sintoma}"
        )
        db.commit()

    reader_11 = csv.reader(file_11)
    for id_causas, pais, causa, afectado, total, porcentaje in reader_11:
        db.execute("INSERT INTO causas (id_causas, pais, causa, afectado, total, porcentaje) VALUES (:id_causas, :pais, :causa, :afectado, :total, :porcentaje)",
                {"id_causas":id_causas, "pais":pais, "causa":causa, "afectado":afectado, "total":total, "porcentaje":porcentaje})
        print(
            f"Added in causas table id_causas:{id_causas}, pais:{pais}, causa:{causa}"
        )
        db.commit()
        
if __name__=="__main__":
    main()


from sqlalchemy import create_engine, MetaData

postgres_url = "postgresql://indexoor:password@indexoor-db:5432/indexoor"


class DB:
    engine = create_engine(postgres_url)
    metadata = MetaData(bind=engine)

    def create_tables(self):
        import tables

        self.metadata.create_all()

def generate_insert_statement(self, data: pd.Series, insert_data: pd.DataFrame):
    """
    Az előző feladata alapján felhasználtam a teljes kódot annyi különbséggel,
    hogy csak a key-t adtam hozzá az insert_statement-hez
    """
    columns = self.generate_dtypes_mapping(data)
    insert_statement = "insert into {table_name} ("
    for key, val in columns.items():
        insert_statement += f"{key}, "

    insert_statement = insert_statement[:-2] + ')'

    """
        inserted_values -ben tárolom a fájlból kiolvasott tartalmat, és ezt nem 
        szépen két ciklussal kinyerem a tartalmát és a végeredményeket az 
        insert_to_db változóban összefűzüm. Az elgondolásom az, hogy amikor megtörténik
        az insert_to_db összefűzése akkor kéne beküldeni az adatbázisba.

        De ha jól értelmezem, akkor itt a file_handler-ben csak fájl műveleteknek kéne lennie,
        ezért szerintem egy másik megoldás az lehetne, ahogy az összefűzött sql kódot egy 
        listába raknám és ezt a listát adná vissza a függvény
        """
    inserted_values = insert_data.values
    value_statement = "values ("
    to_db = ""
    list_of_inserted_data = []
    for idx in range(len(inserted_values)):
        to_db = ""
        for inx in range(len(inserted_values[idx])):
            to_db += str(inserted_values[idx][inx]) + ", "
        full_value = value_statement + to_db[:-2] + ")"
        """insert_to_db - ebben van az összesített adat, amit adatbázisba lehetne küldeni"""
        insert_to_db = insert_statement + " " + full_value
        """vagy listában tárolni"""
        list_of_inserted_data.append(insert_to_db)

    return list_of_inserted_data

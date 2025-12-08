from spb_con import supabase

def new_id(table_name, table_id):
    id_data = supabase.table(table_name).select(table_id).order(table_id, desc=True).limit(1).execute()
    lates_id = id_data.data[0][table_id]

    if len(id_data.data) == 0:
        return 1  
    else:
        return lates_id + 1
    # # Next, insert the class into the 'classes' table if not already present
    #   cursor.execute(
    #     "INSERT INTO classes (class_name) VALUES (%s) ON DUPLICATE KEY UPDATE class_id=LAST_INSERT_ID(class_id)",
    #     (row.class_name,)
    # )
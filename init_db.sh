#!/bin/sh
python -c "
import sqlite3
conn = sqlite3.connect('performance.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS performance (
    timestamp DATETIME NOT NULL
                       DEFAULT CURRENT_TIMESTAMP
                       PRIMARY KEY,
    minutes   INT      NOT NULL
);
''')
conn.commit()
conn.close()
"
exec "$@"

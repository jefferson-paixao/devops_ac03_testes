CREATE TABLE ac3 (
    id INTEGER,
    nome TEXT NOT NULL,
    email TEXT,
    PRIMARY KEY(id)
    );

CREATE TABLE teste as SELECT * FROM pragma_table_info(ac3);
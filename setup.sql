-- Copia esto en el SQL Editor de Supabase
CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

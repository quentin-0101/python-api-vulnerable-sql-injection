setup project : 

execute this on DB
```sql
-- Table des utilisateurs
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username TEXT NOT NULL UNIQUE,
  email TEXT UNIQUE,
  bio TEXT
);

-- Données de test
INSERT INTO users (username, email, bio) VALUES
('alice', 'alice@example.com', 'Pilote de tests'),
('bob', 'bob@example.com', 'DevOps'),
('charlie', 'charlie@example.org', 'Support technique'),
('david', 'david@sample.net', 'Marketing'),
('eve', 'eve@example.io', 'Analyste sécurité')
ON CONFLICT DO NOTHING;


```

in bash
```
docker compose up -d
```


view logs
```
docker logs api -f
```

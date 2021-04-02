INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('Welcome!', 'test' || x'0a' || 'body', 1, '2021-04-01 17:00:00');

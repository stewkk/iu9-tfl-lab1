# rofl-lab1

## Гайд на временную отправку запросов к LLM

Пока не подняли `LLM` на какой-то виртуалке и обращения к БД пока тоже не сделаны
предлагаю поднимать `LLM` локально. Для этого я сделал `compose.yaml`. Поднимать его
очевидно нужно с помощью `docker compose`.

По сути гайд такой:
1) Ставим `Docker` (надеюсь все с этим справятся)
2) С помощью `docker compose` поднимаем `LLM` командой в духе:
```bash
docker compose up --build
```

3) Отправляем промпты на `API` модельки, можно делать это с помощью
`curl` пример можно найти в официальной [доке](https://github.com/ollama/ollama?tab=readme-ov-file#rest-api), либо с помощью самописного
скрипта на `Python`, который лежит в `LLM/tester`
4) Пары вопрос ответ пока что можете сохранять у себя, думаю в будущем просто
заведем файлик `database/database.json`, куда положим все пары

P.S. Убиваем контейнер так: =)
```bash
docker compose down
```
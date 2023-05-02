# MapGPT

## Getting started

1. cd into `frontend`; `npm run dev`
2. in a separate terminal, cd into `backend`; run `source venv/bin/activate`.
3. Then, cd into app and run `uvicorn main:app --reload`.

## Saving requirements after installing

pip freeze | grep -v "file://" > requirements.txt

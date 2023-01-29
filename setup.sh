#/bin/sh
poetry config virtualenvs.in-project true
poetry env use 3.9
source .venv/bin/python
poetry install

git config --local filter.strip-notebook-output.clean "jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to=notebook --stdin --stdout --log-level=ERROR"

# Remove poetry env if needed using the following command
# poetry env remove [path to env]
# To find the env, poetry env info -p
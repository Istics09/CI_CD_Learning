# CI/CD Practice

This is my first CI/CD learning project. I'm learning GitHub Actions by building a small pipeline around a simple Python script.

## What it does

`mailer.py` sends an email with the server's hostname and the current time. Nothing fancy – the point is not the script, but the pipeline around it.

When I push to `main`, GitHub Actions:

1. runs **Ruff** (linting) and **pytest** (tests)
2. if everything passes, deploys the script to my 3 servers over SSH
3. creates the `.env` file on the servers from GitHub Secrets
4. runs the script, so I get an email from each server

## How to run it locally

```bash
pip install python-dotenv pytest ruff
cp .env.proto .env    # then fill in your own SMTP details
python mailer.py
```

Tests and lint:

```bash
pytest -v
ruff check .
```

## Secrets

Passwords, SSH keys and server addresses are not in the repo. They are stored in GitHub Secrets and the workflow reads them from there.

## What I learned so far

- how a GitHub Actions workflow is built (jobs, steps, `needs`)
- using a matrix to deploy to multiple servers
- storing secrets properly instead of hardcoding them (learned this the hard way 🙂)
- writing simple tests with pytest
- fixing lint errors with Ruff

## Next steps

- deploy with a separate user instead of root
- try the same thing with Ansible
- run the script on a schedule (cron)
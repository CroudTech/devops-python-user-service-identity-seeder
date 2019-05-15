# PIP Module seed_identities module

Reads a user service rest api endpoint and seeds an identity server instance.

Usage: seed_identities [OPTIONS]

Options:
  --source TEXT  The source API endpoint  [required]
  --dest TEXT    The destination API endpoint  [required]
  --help         Show this message and exit.

## Example

```
seed_identities --source http://user-service.prod-v3-croud/users --dest http://identityserver.prod-v3-croud/api/users
```
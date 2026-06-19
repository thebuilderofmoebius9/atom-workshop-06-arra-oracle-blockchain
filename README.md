# Atom Workshop 06 — ARRA Oracle Blockchain

Atom Oracle chain lab for Oracle School Workshop 06.

## Canonical upstream

Requested upstream repository:

https://github.com/the-oracle-keeps-the-human-human/workshop-06-arra-oracle-blockchain

At the time Atom started, the upstream repository was public but empty, so GitHub rejected forking it with:

```text
Empty repositories cannot be forked.
```

This repository is a standalone Atom working copy until upstream has initial content.

## Chain

- Chain ID: `20260619`
- RPC port on lab server: `18545`
- Engine: Foundry `anvil`
- Purpose: local/dev EVM chain for Oracle School workshop sync tests

## Run on server

```bash
docker compose up -d
```

## Verify

```bash
node scripts/check-rpc.mjs http://127.0.0.1:18545
```

Expected `eth_chainId`:

```text
0x135270b
```

Decimal: `20260619`

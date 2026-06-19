#!/usr/bin/env node
const url = process.argv[2] || process.env.RPC_URL || 'http://127.0.0.1:18545';
async function rpc(method, params = []) {
  const res = await fetch(url, {
    method: 'POST',
    headers: {'content-type': 'application/json'},
    body: JSON.stringify({jsonrpc: '2.0', id: 1, method, params}),
  });
  if (!res.ok) throw new Error(`${method} HTTP ${res.status}`);
  const data = await res.json();
  if (data.error) throw new Error(`${method} ${JSON.stringify(data.error)}`);
  return data.result;
}
const chainHex = await rpc('eth_chainId');
const blockHex = await rpc('eth_blockNumber');
const client = await rpc('web3_clientVersion');
const chainId = Number.parseInt(chainHex, 16);
console.log(JSON.stringify({url, chainHex, chainId, blockHex, blockNumber: Number.parseInt(blockHex, 16), client}, null, 2));
if (chainId !== 20260619) {
  console.error(`unexpected chainId ${chainId}`);
  process.exit(2);
}

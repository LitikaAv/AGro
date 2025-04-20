# ✅ Protocolo Escolhido: Ethereum (EVM + Solidity)

## 📌 Visão Geral
A infraestrutura inicial escolhida para a Blockchain AGro-Orpheus é baseada na **Ethereum Virtual Machine (EVM)**, utilizando a linguagem **Solidity** e o framework **Hardhat** para desenvolvimento de contratos inteligentes.

Essa decisão foi tomada com base na ampla adoção, robustez do ecossistema, facilidade de implementação e compatibilidade com camadas de escalabilidade e interoperabilidade.

---

## 🎯 Justificativas para a Escolha do EVM

### ✅ Ampla Adoção e Comunidade Ativa
- Ethereum é a blockchain com maior base de desenvolvedores.
- Suporte de ferramentas maduras e documentação rica.

### ✅ Compatibilidade com DeFi e DApps
- Integração direta com aplicativos descentralizados existentes.
- Possibilidade de uso de contratos já auditados como base.

### ✅ Ferramentas de Desenvolvimento
- **Hardhat** para compilação, testes e deploy local/testnet.
- Integração com Metamask, Ethers.js, Alchemy, Infura.

### ✅ Facilidade de Interoperabilidade
- Ethereum possui bridges com Cosmos, Polkadot, BSC, Polygon, etc.
- Suporte a protocolos como Chainlink CCIP e LayerZero.

### ✅ Escalabilidade via Layer 2
- Possibilidade de migração futura para Optimistic ou ZK-Rollups.
- Suporte a sidechains para cargas específicas.

---

## 🔧 Ambiente Inicial de Desenvolvimento
- **Linguagem:** Solidity (v0.8+)
- **Framework:** Hardhat
- **Rede de Teste Inicial:** Goerli ou Sepolia
- **Ferramentas Auxiliares:** OpenZeppelin, Ethers.js, dotenv, IPFS

---

## 🚧 Roadmap de Implementação

### 🔹 Fase 1: Setup Inicial
- [ ] Criar estrutura de projeto Hardhat
- [ ] Escrever contrato inteligente AGroToken (ERC-20)
- [ ] Criar script de deploy e scripts de interação

### 🔹 Fase 2: Simulação do Consenso Híbrido
- [ ] Implementar lógica de PoS básica com staking
- [ ] Simular PoA via contratos de autoridade
- [ ] Criar esboço do IVS (Index Vetorialético de Sustentabilidade)

### 🔹 Fase 3: Testnet
- [ ] Deploy em rede de teste (Goerli ou Sepolia)
- [ ] Verificação no Etherscan
- [ ] Teste de desempenho e auditabilidade

---

## 🔗 Considerações Finais
A adoção do **EVM como infraestrutura inicial** permite agilidade, compatibilidade e expansão rápida do ecossistema AGro-Orpheus. O modelo será modular e adaptável para futuras migrações para Cosmos SDK, Substrate ou L2 customizadas.

📌 *Este documento será atualizado conforme avanços no roadmap e feedback da comunidade.*

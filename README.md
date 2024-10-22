![Hummingbot](https://i.ibb.co/X5zNkKw/blacklogo-with-text.png)

----
[![Jenkins](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-master_branch&subject=jenkins:master)](https://jenkins-02.coinalpha.com/job/hb_test-master_branch)
[![Jenkins](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-development_branch&subject=:development)](https://jenkins-02.coinalpha.com/job/hb_test-development_branch)
[![Discord](https://img.shields.io/discord/530578568154054663.svg?color=768AD4&label=discord&logo=https%3A%2F%2Fdiscordapp.com%2Fassets%2F8c9701b98ad4372b58f13fd9f65f966e.svg)](https://discord.hummingbot.io/)
[![License](https://img.shields.io/badge/License-Apache%202.0-informational.svg)](https://github.com/bitcoinsfacil/marketmaker_nmbi/blob/master/LICENSE)
[![Twitter Follow](https://img.shields.io/twitter/follow/hummingbot_io.svg?style=social&label=hummingbot)](https://twitter.com/hummingbot_io)

Hummingbot is an open-source project that integrates cryptocurrency trading on both **centralized exchanges** and **decentralized protocols**. It allows users to run a client that executes customized, automated trading strategies for cryptocurrencies.

We created hummingbot to promote **decentralized market-making**: enabling members of the community to contribute to the liquidity and trading efficiency in cryptocurrency markets.

## Supported centralized exchanges

| logo | id | name | ver | doc|
|:---:|:---:|:---:|:---:|:---:|
| [![binance](https://i.ibb.co/m0YDQLd/Screen-Shot-2019-03-14-at-10-53-42-AM.png)](https://www.binance.com/?ref=10205187) | binance | [Binance](https://www.binance.com/) | * | [API](https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md) | [![Build Status](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-exchange_binance&subject=test)](https://jenkins-02.coinalpha.com/job/hb_test-exchange_binance/) |
| [![COINBASE](https://i.ibb.co/h9JdGDW/cbp.jpg)](https://pro.coinbase.com/) | coinbase_pro | [Coinbase Pro](https://pro.coinbase.com/) | * | [API](https://docs.pro.coinbase.com/) | [![Build Status](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-exchange_coinbase&subject=test)](https://jenkins-02.coinalpha.com/job/hb_test-exchange_coinbase/) |
|<img src="https://www.usenix.org/sites/default/files/sponsor_images/huobi_600x240.png" alt="Huobi Global" width="80" height="30" />| huobi | [Huobi Global](https://www.hbg.com) | 1 | [API](https://huobiapi.github.io/docs/spot/v1/en/) | [![Build Status](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-exchange_huobi&subject=test)](https://jenkins-02.coinalpha.com/job/hb_test-exchange_huobi/) |
|<img src="https://www.trustnodes.com/wp-content/uploads/2019/06/bittrex-1175x500.png" alt="Bittrex Global" width="80" height="30" />| bittrex | [Bittrex Global](https://global.bittrex.com/) | 1 | [API](https://bittrex.github.io/api/v1-1) |

## Supported decentralized exchanges

| logo | id | name | ver | doc|
|:---:|:---:|:---:|:---:|:---:|
| [![Radar Relay](https://i.ibb.co/7RW75mf/Screen-Shot-2019-03-14-at-10-47-07-AM.png)](https://radarrelay.com/) | radar_relay | [Radar Relay](https://radarrelay.com/) | 2 | [API](https://developers.radarrelay.com/api/trade-api) | [![Build Status](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-exchange_radar_relay&subject=test)](https://jenkins-02.coinalpha.com/job/hb_test-exchange_radar_relay/) |
| [![DDEX](https://i.ibb.co/Lrpps2G/Screen-Shot-2019-03-14-at-10-39-23-AM.png)](https://ddex.io/) | ddex | [DDEX](https://ddex.io/) | 3 | [API](https://docs.ddex.io/) | [![Build Status](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-exchange_ddex&subject=test)](https://jenkins-02.coinalpha.com/job/hb_test-exchange_ddex/) |
| [![IDEX](https://i.ibb.co/k97fzrg/idex.png)](https://idex.market/) | idex | [IDEX](https://idex.market/) | * | [API](https://docs.idex.market/) | |

## Community contributed exchanges

| logo | id | name | ver | doc| maintainer |
|:---:|:---:|:---:|:---:|:---:|:---:|
| [![Bamboo Relay](https://i.ibb.co/1sPt940/Screen-Shot-2019-06-06-at-17-50-04.png)](https://bamboorelay.com/) | bamboo_relay | [Bamboo Relay](https://bamboorelay.com/) | * | [API](https://sra.bamboorelay.com/) | [dex@bamboorelay.com](mailto:dex@bamboorelay.com)
| [![Dolomite](https://firebasestorage.googleapis.com/v0/b/dolomite-landing-page.appspot.com/o/images%2FDolomite_name_and_logo_black_1_10.png?alt=media)](https://dolomite.io/) | dolomite | [Dolomite](https://dolomite.io/) | 1 | [API](https://docs.dolomite.io/) | [corey@dolomite.io](mailto:corey@dolomite.io)

## Currently available strategies

| Strategy | Test |
|--|--|
| [Pure market making](https://docs.hummingbot.io/strategies/pure-market-making/) | [![Build Status](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-strategy_pure_mm&subject=test)](https://jenkins-02.coinalpha.com/job/hb_test-strategy_pure_mm/) |
| [Cross exchange market making](https://docs.hummingbot.io/strategies/cross-exchange-market-making/) | [![Build Status](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-strategy_xemm&subject=test)](https://jenkins-02.coinalpha.com/job/hb_test-strategy_xemm/) |
| [Arbitrage](https://docs.hummingbot.io/strategies/arbitrage/) | [![Build Status](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-strategy_arbitrage&subject=test)](https://jenkins-02.coinalpha.com/job/hb_test-strategy_arbitrage/) |
| [Discovery](https://docs.hummingbot.io/strategies/discovery/) | [![Build Status](https://jenkins-02.coinalpha.com/buildStatus/icon?job=hb_test-strategy_discovery&subject=test)](https://jenkins-02.coinalpha.com/job/hb_test-strategy_discovery/) |

## Getting Started

### Learn more about Hummingbot

- [Hummingbot website](https://hummingbot.io)
- [Documentation](https://docs.hummingbot.io)
- [Read our blog](https://www.hummingbot.io/blog)
- [Whitepaper](https://hummingbot.io/whitepaper.pdf)
- [FAQs](https://docs.hummingbot.io/faq/)
- [Roadmap](https://docs.hummingbot.io/roadmap/): including planned features

### Install Hummingbot

- [Installation guide](https://docs.hummingbot.io/installation/)
- [Installation scripts](./installation/)

## Contributions

We welcome contributions from the community:
- **Code contributions** via [pull requests](./pulls).
- **Bug reports** / **feature requests** through [github issues](./issues).
- **Development discussions**: visit the [Hummingbot Dev Forum](https://forum.hummingbot.io).
- [**Hummingbot code base**](./hummingbot): located in the `hummingbot/` folder
- When contributing, please review the [contributing guidelines](CONTRIBUTING.md).

## Contact

### Hummingbot community
- Join us on [Discord](https://discord.coinalpha.com).
- Follow Hummingbot on [Twitter](https://twitter.com/hummingbot_io).

### CoinAlpha

Hummingbot was created and is maintained by [CoinAlpha](https://www.coinalpha.com).

- **General**: contact us at [dev@hummingbot.io](mailto:dev@hummingbot.io) or join our [Discord server](https://discord.coinalpha.com).
- **Business inquiries**: contact us at [partnerships@hummingbot.io](mailto:partnerships@hummingbot.io).

## Legal

- **License**: Hummingbot is licensed under [Apache 2.0](./LICENSE).
- **Data collection**: read important information regarding [Hummingbot Data Collection](DATA_COLLECTION.md).

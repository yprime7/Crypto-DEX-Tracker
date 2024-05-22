from dexscreener import DexscreenerClient

import asyncio


async def main():
    client = DexscreenerClient()
    print("Fetching token pair...")
    pair = await client.get_token_pair_async("harmony", "0xcd818813f038a4d1a27c84d24d74bbc21551fa83")
    print("Token pair:", pair)

    print("Fetching token pairs...")
    # ETH = 0x2170Ed0880ac9A755fd29B2688956BD959F933F8
    pairs = await client.get_token_pairs_async("0x2170Ed0880ac9A755fd29B2688956BD959F933F8")
    print("Token pairs:", pairs)

    print("Searching for WBTC pairs...")
    search = await client.search_pairs_async("SOL")
    print("WBTC pairs:", search)
'''
    pair = await client.get_token_pair_async("harmony", "0xcd818813f038a4d1a27c84d24d74bbc21551fa83")

    pairs = await client.get_token_pairs_async("0x2170Ed0880ac9A755fd29B2688956BD959F933F8")

    search = await client.search_pairs_async("WBTC")

'''
    

if __name__ == "__main__":
    asyncio.run(main())

# asyncio.get_event_loop().run_until_complete(main())

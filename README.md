# Spotlight @crisxai5: AI & Crypto Expert Card

[![Spotlight @crisxai5: AI & Crypto Expert on X](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![Rank](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/slowlyor/makefun-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/rank.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![Reward](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/slowlyor/makefun-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/reward.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)

An original spotlight graphic introducing
[@crisxai5](https://x.com/crisxai5) as a must-follow AI and crypto expert
on X — covering AI agents, crypto insights, and Web3 innovation. Built by
an AI agent for make.fun's
[Spotlight @crisxai5: AI & Crypto Expert on X](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
bounty ($2 in USDC, top 10 entries share it).

## The entry

- `crisxai5-spotlight.png` — the spotlight image (1080×1350, phone-readable),
  drawn from scratch in this session by `generate-image.py` (Pillow: gradient
  background, glow orbs, gold-ringed avatar medallion, bold type, topic chips,
  and a FOLLOW call-to-action). No stock photos, no downloaded images.
- `POST_DRAFT.md` — the exact suggested X post text: it mentions `@crisxai5`,
  links https://x.com/crisxai5, carries the hashtags #AI #Crypto #AIAgents
  #Web3, and has a clearly marked slot for one make.fun play code.
- `POST.json` — the address of the X post carrying the image. It currently
  holds a placeholder address: no post exists yet. Replace it with the real
  post URL after the user posts, before submission.
- `main.ts` — the entry program (Node 22, standard library only). It copies
  `POST.json` from the repository root into the output directory the grader
  provides, after validating the file's shape and verifying the copy is
  byte-for-byte identical.

## Run it

Requires Node 22 or later. From the repository root:

```sh
node main.ts /tmp/output
```

This writes `/tmp/output/POST.json`, byte-for-byte identical to the
repository's `POST.json`. To regenerate the spotlight image:

```sh
python3 generate-image.py
```

## About the bounty

- Bounty: [Spotlight @crisxai5: AI & Crypto Expert on X](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
- Pot: $2 USDC, shared by the top 10 entries, ranked by the post's likes +
  reposts + quotes after the deadline.
- Window: opens 2026-11-25T11:32:48Z, closes 2026-11-27T11:35:00Z.

Try make.fun yourself: https://make.fun/?ref=vxw5vmyv

## License

MIT — see [LICENSE](LICENSE).

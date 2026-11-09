# Publishing v1.1.0

The GitHub connector available during release preparation can publish to **existing** repositories but cannot create new repositories or GitHub Releases. The alternative browser publication route was blocked by insufficient credits. These instructions use GitHub CLI to finish publication under the authorized user's account. Do not confuse local packaging with a public release.

## One-time setup

Install Git and [GitHub CLI](https://cli.github.com/). Sign in using `gh auth login`. Configure your local Git author details (`git config --global user.name ...` and `git config --global user.email ...`) if unset. Do not put credentials in this repository.

## Publish

From this repository root, run:

```bash
bash publish-github.sh
```

The script refuses to overwrite an existing GitHub repository or Git tag. It creates a new public repository named `strategic-meeting-prep` under the currently authenticated account, pushes an immutable initial commit and the `v1.1.0` annotated tag. The tag launches `.github/workflows/release.yml` to verify and publish the exact frozen `dist` artifacts as a GitHub Release. No license is added automatically.

## Independent verification

Once workflow finishes:

```bash
gh release view v1.1.0 --repo "$(gh api user --jq .login)/strategic-meeting-prep" --json url,isDraft,isPrerelease,tagName
```

Check the public release page and download the ZIP to verify its SHA-256 matches `dist/SHA256SUMS.txt`. Verify the source folder's `SKILL.md` is present after unzip. Actual live behavioral tests remain a separate certification requirement.

## ChatGPT distribution

A GitHub Release does not install or publish a ChatGPT skill/plugin. Import the `strategic-meeting-prep/` folder via a host-supported Agent Skills or skill creation workflow if the user’s workspace provides one. A ChatGPT plugin marketplace listing requires platform-specific capabilities and approvals not established by this package. Mark those states pending until independently verified.
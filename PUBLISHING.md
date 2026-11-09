# Publishing Strategic Meeting Prep v1.1.0

## Current state

The dedicated public repository is available and contains documentation, core skill instructions, an attestation, and the automated `.github/workflows/complete-release.yml`. The **frozen installable ZIP is not yet in GitHub**. Do not claim the GitHub Release is live until it appears on the public Releases page.

## One remaining source-upload step

1. Download the **original, frozen** `strategic-meeting-prep-v1.1.0.zip` archive from the ChatGPT release conversation.
2. Open [GitHub upload to `dist/`](https://github.com/evansmusitu/strategic-meeting-prep/upload/main/dist), select the ZIP, and commit directly to `main`, keeping the filename unchanged.
3. Confirm the archive's SHA-256 is `742ec8009110e7e918ff7990eb51dd7325564456f7c7d57b3110c23f56c89e33`.
4. Watch [the finalization Actions workflow](https://github.com/evansmusitu/strategic-meeting-prep/actions/workflows/complete-release.yml). It checks the exact hash, extracts the skill source, reruns deterministic gates, restores the frozen benchmark snapshot, checks every source byte, commits source, creates `v1.1.0`, and invokes `gh release create`.

## Independent verification

Open [Releases](https://github.com/evansmusitu/strategic-meeting-prep/releases/tag/v1.1.0) and verify `v1.1.0` is public (not a draft), the archive can be downloaded, and the archive SHA-256 matches the frozen hash. A successful workflow run is not sufficient unless the public release is visible.

```bash
gh release view v1.1.0 --repo evansmusitu/strategic-meeting-prep --json url,isDraft,isPrerelease,tagName
```

## Certification and license

Static and benchmark-coverage tests passed locally, but no live model behavior baseline or blinded holdout has been executed. Behavioral certification is inconclusive. No public reuse license has been selected. A GitHub Release does not itself install the skill in ChatGPT or list a plugin in any marketplace.

# Release status

The verified v1.1.0 ZIP is not yet present on GitHub; the GitHub Release is not published. Upload the exact `strategic-meeting-prep-v1.1.0.zip` (SHA-256: `742ec8009110e7e918ff7990eb51dd7325564456f7c7d57b3110c23f56c89e33`) to `dist/` on `main` to trigger `.github/workflows/complete-release.yml`. The action verifies it, extracts and tests its exact source, tags and publishes the release. Behavioral certification is pending.

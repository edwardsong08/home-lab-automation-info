# Home Lab Automation Information

Public app information, privacy policy and personal-use terms for Home Lab n8n Logs.

Live site: https://automation.edsong.xyz

## Editing and deployment

Edit `index.html` and commit to `main` to update public wording. Keep the data-use description truthful and update the policy date for meaningful changes.

Coolify builds this repository using the root `Dockerfile` and the existing GitHub App integration. Pushes to `main` trigger automatic deployment. The container serves `/`, `/privacy`, `/terms`, and `/health` on port 8080. GET and HEAD are supported; other paths return 404.

Runtime limits are 64 MB RAM and 0.25 CPU. The image runs as a non-root user. Coolify applies a read-only filesystem and drops Linux capabilities. No persistent storage or application secrets are needed. Coolify management remains private; the existing GitHub webhook integration is reused.

This public repository contains no credentials, private home-lab records or workflow data. Never add them.

## Rollback and portability

Revert a Git commit on `main` to deploy prior content, or use Coolify rollback. A stopped previous static service is retained temporarily for migration rollback; avoid running both with the same domain.

On another container platform, build the Dockerfile and route HTTPS to container port 8080. Preserve non-root execution and resource/security limits.

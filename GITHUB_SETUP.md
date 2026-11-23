# GitHub Authentication Setup Guide

## How to Connect GitHub Authentication

Since I cannot perform interactive authentication, you need to manually connect GitHub to push the code.

### Option 1: Device Flow (Recommended)

```bash
# Install GH CLI (if not already installed)
# For Debian/Ubuntu:
type -p dnf &>/dev/null && sudo dnf install gh -y
type -p yum &>/dev/null && sudo yum install gh -y
type -p apt-get &>/dev/null && sudo apt-get update && sudo apt-get install gh -y

# Or download binary directly
mkdir -p ~/bin
curl -sL https://github.com/cli/cli/releases/download/v2.44.0/gh_2.44.0_linux_amd64.tar.gz -o /tmp/gh.tar.gz
tar -xzf /tmp/gh.tar.gz -C /tmp
sudo /tmp/gh_2.44.0_linux_amd64/gh auth login --webbrowser
```

The `--webbrowser` flag will:
1. Print a URL to your terminal
2. Open it in your default browser
3. You approve the GitHub authorization
4. Authentication completes automatically

### Option 2: Personal Access Token (PAT)

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Fine-grained tokens"
3. Set permissions:
   - Repository: Read and write
   - Metadata: Read
4. Copy the token
5. Run:
```bash
# Store credential
echo "https://YOUR_TOKEN@github.com" > ~/.git-credentials
git config credential.helper store
```

### Option 3: SSH Keys (Alternative)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "aloknidhi406@gmail.com"

# Add to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add to GitHub: https://github.com/settings/keys

# Change remote URL to use SSH
git remote set-url origin git@github.com:aloknidhi/Simple_project.git
```

## Verify Authentication

```bash
# Check if you're authenticated
gh auth status

# Or try a push
git push origin main
```

## Current Repository State

- **Commits**: 4 commits made locally
- **Pending**: Push to GitHub
- **Files**: 13 files, ~50KB total

### Commits Awaiting Push
1. Initial setup
2. `docs: add comprehensive project setup and documentation` - 11 files
3. `docs: add .gitignore and update day 1 progress`
4. `docs: add issue and PR templates for project management`

## Troubleshooting

### Error: "could not read Username"
This means credentials aren't cached. Run one of the options above.

### Error: "Authentication failed"
Check that your token/credentials are valid and haven't expired.

### Need Help?
1. Check GitHub token permissions
2. Verify repository exists at `aloknidhi/Simple_project`
3. Ensure you have write access to the repository

---
*Generated: November 23, 2024*
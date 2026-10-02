# Migration to Grok-ready

The project owner has designated https://github.com/vitalitychems-dot/Grok-ready as the final consolidated repository, superseding TX as the destination.

## Status: consolidation in progress — not yet verified complete

All listed source repositories and local subrepl branch contributions are in scope. Unique working functionality must be reconciled into one canonical tree; identical content and redundant versions must not be copied into parallel application trees. Combine README instructions without losing distinct setup requirements. Convert non-UI images into accurate written summaries; retain images required by UI/themes. Do not publish credentials, personal records, private vault contents, or generated chat/audit data.

## Instructions for agents

1. Preserve this repository and all existing branches. Do not delete, force-push, or announce migration complete.
2. Report outstanding unique changes and source commit IDs in Grok-ready issues or pull requests. Do not lose work in progress.
3. Once a verified consolidated baseline exists, fetch Grok-ready main and create a focused agent branch from it. Submit reviewed pull requests rather than overwriting shared main.
4. Before confirming migration, compare your contributions against the consolidated commit, run the applicable checks, and record missing work or blockers.
5. Record an explicit sign-off in Grok-ready identifying the source repository/branches, verified target commit, and verification results. A notice or silence is not agreement.

## Deletion gate

No source repository may be deleted while any contribution or agent sign-off is outstanding. Preserve backups and confirm the exact deletion target with the owner after all agents agree the migration is complete.

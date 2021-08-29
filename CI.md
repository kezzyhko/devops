# Best practices about CI

This file contains some best practices I found about the CI:
* Workflow should not require manual input
* Workflows should not include passwords and tokens, there are github secrets for that
* Code should be tested before publishing
* CI should be the only way to publish app to the production
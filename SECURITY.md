# Security Policy

## Supported Versions

Only the latest commit on the `main` branch is supported.

## Reporting a Vulnerability

If you find a security issue, please open a GitHub issue with the label
`security` and a clear description. Do not include any private keys, seed
phrases, passwords, or real wallet data in your report.

## Scope Notes

This tool runs locally with the Python standard library only. It makes no
network requests, stores no seed phrases or private keys, and never moves
funds. Validators in this project only check formats or counts; they never
use, transmit, or persist secret material.

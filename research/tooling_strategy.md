# Project Chimera — Tooling Strategy (MCP)

## Purpose

This document defines the **developer-facing MCP tools** used during the
design, specification, and implementation of Project Chimera.

These tools empower the human developer (FDE) and the IDE-based AI copilot,
not the runtime Chimera agents.

---

## Tooling Philosophy

- Development tools ≠ Agent skills
- MCP tools are **assistive**, not autonomous
- Every tool must increase:
  - Traceability
  - Safety
  - Spec adherence

---

## Selected MCP Servers

### 1. filesystem-mcp

**Purpose:**  
Enable safe, structured file creation and editing inside the repository.

**Capabilities:**
- Read/write files
- Create directories
- Enforce project structure (specs/, skills/, research/)

**Why it matters for Chimera:**
- Prevents undocumented changes
- Keeps specs, rules, and code aligned
- Enables spec-first workflows

---

### 2. git-mcp

**Purpose:**  
Provide version control awareness and discipline.

**Capabilities:**
- View git status
- Create commits
- Inspect diffs
- Reference commit history

**Why it matters for Chimera:**
- Architectural decisions must be traceable
- Enables rollback and auditability
- Aligns with professional engineering workflows

---

### 3. (Optional / Future) memory-mcp

**Purpose:**  
Persist architectural decisions and long-term context.

**Potential Capabilities:**
- Store design rationales
- Recall prior constraints
- Prevent repeated mistakes

**Status:** Not required for early phases

---

## Explicit Non-Goals

- MCP tools are NOT used by runtime agents
- MCP tools do NOT make autonomous decisions
- MCP tools do NOT bypass specs or rules

---

## Summary

MCP tooling is intentionally minimal and conservative.

The goal is not speed — the goal is **correctness, clarity, and control**.

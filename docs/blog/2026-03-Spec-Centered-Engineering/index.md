---
blogpost: true
date: 2026-03-20
language: English
tags: CC-BY-SA-4.0, Mechatronics, Software Architecture,
---

# «Article» Specification-Centered Engineering

**A Resurrection of Engineering Discipline in the Age of Heavyweight Modeling Tools**

Revision 2 — Alexander Mann-Wahrenberg (basejumpa) — 2026

*License: CC BY-SA 4.0*

---

## 1. Introduction

In many modern engineering environments, communication has gradually shifted away from precise, written specifications toward model-centric tooling: proprietary environments such as Enterprise Architect, IBM Rational Rhapsody, IBM DOORS, or PTC Integrity. While these tools promise integrated traceability, visual richness, and process compliance, they frequently fail to establish what engineering fundamentally requires:

> **A shared, precise, and verifiable understanding of a system.**

This article proposes a return to a more disciplined approach: **Specification-Centered Engineering**, grounded in **Docs-as-Code** practices. It does not reject modeling or diagrams — on the contrary, it embraces them — but places them in their proper role as *supporting instruments*, not as the primary carriers of meaning.

---

## 2. The Problem: When the Tool Becomes the Truth

A common pattern in systems and software engineering organizations is the elevation of the modeling tool to the role of authoritative source of truth. When the model lives inside Enterprise Architect or Rhapsody, several problems emerge organically:

- Implicit assumptions remain locked inside tool-specific constructs, invisible to anyone without a license or familiarity with the tool.
- Semantics are inferred from visual layout rather than defined in explicit text.
- Different stakeholders derive different meanings from the same diagram, without any written specification to arbitrate.

The result is a dangerous illusion:

> **The tool's coherence is mistaken for semantic correctness.**

A model that validates cleanly inside Enterprise Architect may still be ambiguous, incomplete, or wrong — because the tool enforces structural rules, not engineering meaning.

---

## 3. Heavyweight Modeling Tools: Genuine Value and Genuine Risk

It would be unfair to dismiss tools like Enterprise Architect, Rhapsody, or DOORS outright. They offer real capabilities:

- Cross-artifact traceability (requirements → architecture → test cases)
- Formal model execution and simulation in Rhapsody
- Integration with regulated-industry workflows (ISO 26262, DO-178C, IEC 61508)
- Structured management of large requirement sets in DOORS

However, these benefits come with significant costs that are rarely acknowledged openly:

### 3.1 Opacity and Lock-in

Model artifacts in these tools are stored in proprietary binary or semi-proprietary formats (`.eap`, `.mdzip`, `.rpy`). Reviewing a change means opening the tool. Diffing two versions requires vendor-specific utilities, if it is possible at all. The information is effectively trapped.

### 3.2 The Diagram Substitutes for the Specification

In practice, what gets communicated between teams is not the underlying model data, but exported diagrams — PDFs, PNGs, PowerPoint slides. The recipient sees a picture, not a model. The tool's sophistication evaporates at the point of communication.

### 3.3 Tool-Driven Modeling

Engineers learn to model in the way the tool permits, not in the way the problem demands. Rhapsody encourages a particular style of statechart. Enterprise Architect shapes how components and interfaces are expressed. The tool's metamodel silently constrains the engineering thinking.

### 3.4 Maintenance Burden

Large EA or Rhapsody models accumulate technical debt faster than source code. Inconsistencies between diagrams, obsolete elements, broken links, and duplicated content are common. The cost of keeping a heavyweight model synchronized with reality is routinely underestimated.

---

## 4. Modeling vs. Diagrams: A Necessary Distinction

Before proposing an alternative, it is essential to separate three often conflated concepts:

- **Modeling**: the intellectual act of abstracting and structuring reality
- **Model**: the abstract representation of a system
- **Diagram**: one possible visualization of that model

UML, SysML, and similar notations are languages, not drawing tools. Their essence lies in semantics: classifiers, relationships, states, transitions, and constraints. These can, in principle, be expressed entirely in text.

A useful thought experiment:

> If a domain expert can understand a model purely from a precise verbal description — and reconstruct it without ever seeing the diagram — then the model exists independently of its graphical representation.

This leads to a key insight that heavyweight tools tend to obscure:

> **The model is not the diagram. The diagram is only a view. And the tool is neither.**

---

## 5. The Core Principle: The Specification is the Source of Truth

Specification-Centered Engineering establishes a clear hierarchy:

**Text (Normative Layer)**
- Defines meaning
- Specifies behavior, structure, and constraints
- Serves as the authoritative reference
- Lives in version control, readable without any tool license

**Diagrams (Explanatory Layer)**
- Provide overview and intuition
- Support understanding, but do not define truth
- Embeddable as figures in the document

**Tools (Operational Layer)**
- Assist in creating and managing artifacts
- Must not hold the model hostage in a proprietary format
- Must not dictate structure or meaning

In case of conflict:

> **The written specification prevails.**

---

## 6. Why Text Matters

### 6.1 Precision

Text allows for explicit definition of conditions, constraints, temporal behavior, and edge cases. For example:

> "If condition A and B hold, action C must occur within 200 ms."

Such a statement cannot be encoded unambiguously in a diagram alone, and in a heavyweight model it would require constraint language (OCL, textual SysML) that most users never employ.

### 6.2 Sequential Reasoning

Text supports argumentation, causal explanation, and traceable logic. Engineering is not only about structure but about *why* decisions are made — and a diagram never explains its own rationale.

### 6.3 Reviewability and Versioning

Text integrates naturally with version control systems, code reviews, and diff-based discussions. A pull request on a Markdown specification is reviewable by any engineer with a browser. A pull request on an `.eap` file is not reviewable at all.

---

## 7. Docs-as-Code as the Practical Alternative

Docs-as-Code provides the technical foundation for Specification-Centered Engineering:

- Specifications written in Markdown, MyST, reStructuredText, or AsciiDoc
- Stored in version control alongside source code
- Reviewed and evolved through standard pull request workflows
- Built and published via CI pipelines
- Diagrams embedded as figures, generated from text-based sources (PlantUML, Mermaid, draw.io exports)

This is not a rejection of diagrams or models. PlantUML and Mermaid can generate UML class diagrams, sequence diagrams, and state machines from plain text. The diagram is rendered from the specification, not the reverse. The text is the source of truth; the picture is its output.

Compared to heavyweight tools:

- No license required to read, review, or contribute
- Full diff and history available in any Git client
- Specification and implementation live in the same repository
- No proprietary format lock-in

---

## 8. Addressing Regulated Industries

A common objection is that regulated industries — automotive (ISO 26262), aerospace (DO-178C), medical devices (IEC 62304) — mandate toolchains that require certified tools, making Docs-as-Code impractical.

This objection deserves a direct response. The regulations mandate traceability, auditability, and rigor — not specific tools. The assumption that DOORS or Polarion is required is often a cultural artifact, not a regulatory one. Several teams in regulated domains have successfully adopted text-based specification workflows with appropriate tooling for traceability (e.g., Sphinx-Needs, Doorstop).

Moreover, even in environments where heavyweight tools are mandated, the core discipline of Specification-Centered Engineering still applies: the written requirement or specification is the truth, and the tool is a container — not the model itself.

---

## 9. The Blind Expert Test

A practical validation technique for any specification or model is the *Blind Expert Test*:

> A model is sound if it can be explained verbally to a domain expert, who can then reconstruct it without seeing any diagram or opening any tool.

Failure of this test indicates missing semantics, reliance on visual or tool-specific cues, or insufficient precision. It ensures that the model resides in shared understanding — not in a proprietary artifact.

---

## 10. Anti-Patterns to Avoid

**Tool-Driven Modeling**
Modeling performed to satisfy tooling capabilities or license utilization rather than engineering needs. The tool shapes the model, not the problem.

**Diagram-Only Communication**
Use of exported diagrams without accompanying textual definitions. The recipient cannot recover the semantics from the picture alone.

**The Living Model Fallacy**
The belief that because the model is "alive" inside a tool — linked, traceable, and visually consistent — it is therefore correct and shared. Tooling consistency is not semantic correctness.

**Model Inflation**
Creation of large, elaborate models in Enterprise Architect or Rhapsody that exceed human comprehension and whose maintenance cost exceeds their communication value.

**Detached Modeling**
Models that are not connected to implementation, testing, or system behavior — often a consequence of the model living in a separate tool from the code.

---

## 11. A Cultural Shift

Adopting Specification-Centered Engineering requires a change in mindset that goes beyond tooling:

> We are not populating a model database.
> We are building shared understanding.

> We are not producing tool-validated diagrams.
> We are optimizing for correctness and clarity.

> The tool works for us.
> We do not work for the tool.

---

## 12. Conclusion

Specification-Centered Engineering is not a rejection of modeling, UML, SysML, or structured methods. It is a rebalancing — specifically a rejection of the pattern where a proprietary modeling tool becomes the epistemic authority of a system's design.

It restores:

- Semantics over representation
- Clarity over visual sophistication
- Openness over tool lock-in
- Understanding over artifact production

By grounding engineering communication in precise, written specifications — maintained in version control, reviewable by all, and independent of any tool license — and by treating diagrams as generated views rather than authoritative sources, we reduce ambiguity, improve alignment, and ultimately build better systems.

> **Think in models.**
> **Express in text.**
> **Illustrate with diagrams.**
> **Validate against reality.**
> **Own your specification.**

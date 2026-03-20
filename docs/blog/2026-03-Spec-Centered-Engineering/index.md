---
blogpost: true
date: 2026-03-20
language: English
tags: CC-BY-SA-4.0, Mechatronics, Software Architecture,
---

# «Article» Specification-Centered Engineering

**A Resurrection of Engineering Articles in the Age of Docs-as-Code**

- License: CC BY-SA-4.0
- Copyright: Alex Mann-Wahrenberg (basejumpa) 2026

## 1. Introduction

In many modern engineering environments, communication has gradually shifted away from precise, written specifications toward visually appealing artifacts: slide decks, UML diagrams, and large tool-centered models. While these artifacts often create the impression of clarity and alignment, they frequently fail to establish what engineering fundamentally requires:

> **A shared, precise, and verifiable understanding of a system.**

This article proposes a return to a more disciplined approach: **Specification-Centered Engineering**, grounded in **Docs-as-Code** practices. It does not reject modeling or diagrams—on the contrary, it embraces them—but places them in their proper role as *supporting instruments*, not as the primary carriers of meaning.

## 2. The Problem: When Representation Replaces Understanding

A common saying states: *“A picture says more than a thousand words.”* While this may hold true in art, it is deeply problematic in engineering.

A picture may indeed evoke many interpretations—but not necessarily the **same** interpretation in every observer. In engineering, however, divergence in interpretation is not richness; it is risk.

When diagrams or models are used as the sole medium of communication:

- implicit assumptions remain unspoken  
- semantics are inferred rather than defined  
- different stakeholders derive different meanings  

The result is a dangerous illusion:

> **Visual coherence is mistaken for semantic correctness.**

This often leads to systems that appear well-designed in meetings but fail during implementation, integration, or operation.

## 3. Modeling vs. Diagrams

It is essential to distinguish between three often conflated concepts:

- **Modeling**: the intellectual act of abstracting and structuring reality  
- **Model**: the abstract representation of a system  
- **Diagram**: one possible visualization of that model  

UML, for example, is a **language**, not a drawing tool. Its essence lies in its *semantics*: classifiers, relationships, states, transitions, and constraints. These can, in principle, be expressed entirely in text.

A useful thought experiment illustrates this:

> If a domain expert can understand a model purely from a precise verbal description—and reconstruct it without ever seeing the diagram—then the model exists independently of its graphical representation.

This leads to a key insight:

> **The model is not the diagram. The diagram is only a view.**

## 4. The Core Principle: The Specification is the Source of Truth

Specification-Centered Engineering establishes a clear hierarchy:

Text (Normative Layer)

- Defines meaning  
- Specifies behavior, structure, and constraints  
- Serves as the authoritative reference  

Diagrams (Explanatory Layer)

- Provide overview and intuition  
- Compress complex relationships into visual form  
- Support understanding, but do not define truth  

Tools (Operational Layer)

- Assist in creating and managing artifacts  
- Must not dictate structure or meaning  

In case of conflict:

> **The written specification prevails.**

## 5. Why Text Matters

Written specifications offer several essential properties:

### 5.1 Precision

Text allows for explicit definition of:

- conditions and constraints  
- temporal behavior  
- edge cases  

For example:
> “If condition A and B hold, action C must occur within 200 ms.”

Such statements are difficult to encode unambiguously in diagrams alone.

### 5.2 Sequential Reasoning

Text supports:

- argumentation  
- causal explanation  
- traceable logic  

Engineering is not only about structure, but about *why* decisions are made.

### 5.3 Reviewability and Versioning

Text integrates naturally with:

- version control systems  
- code reviews  
- diff-based discussions  

This enables:

- transparency  
- traceability  
- collaborative refinement  

## 6. The Role of Diagrams

Diagrams remain highly valuable—when used correctly.

They are particularly effective for:

- system overviews  
- structural relationships  
- communication across disciplines  

However, they must be treated as:

> **Lossy compression of the underlying model.**

They omit detail for the sake of clarity. Therefore:

- every diagram must be accompanied by text  
- no diagram should stand alone  
- all semantics must be recoverable from the specification  

A simple rule applies:

> **If a diagram cannot be translated into precise text, it is not a reliable model.**

## 7. The Blind Expert Test

A practical validation technique is the *Blind Expert Test*:

> A model is sound if it can be explained verbally to an expert, who can reconstruct it without seeing the diagram.

Failure of this test indicates:

- missing semantics  
- reliance on visual cues  
- insufficient precision  

This test ensures that the model resides in **shared understanding**, not in graphical artifacts.

## 8. Anti-Patterns to Avoid

Specification-Centered Engineering explicitly rejects several common practices:

Tool-Driven Modeling
: Modeling performed to satisfy tooling capabilities rather than engineering needs.

Diagram-Only Communication
: Use of diagrams without accompanying textual definitions.

Visual Persuasion
: Relying on appealing visuals to replace rigorous reasoning.

Model Inflation
: Creation of large, complex models that exceed human comprehension.

Detached Modeling
: Models that are not connected to implementation, testing, or system behavior.

## 9. Docs-as-Code as an Enabler

Docs-as-Code provides the technical foundation for this approach:

- specifications written in Markdown, MyST, or AsciiDoc  
- stored in version control systems  
- reviewed and evolved like source code  

This enables:

- consistency between documentation and implementation  
- collaborative authorship  
- continuous refinement  

Diagrams can be embedded as figures, but remain subordinate to the text.

## 10. A Cultural Shift

Adopting Specification-Centered Engineering requires a change in mindset:

> We are not producing diagrams.  
> We are building shared understanding.

> We are not optimizing for visual appeal.  
> We are optimizing for correctness and clarity.

> We are not art critics.  
> We are engineers.

## 11. Conclusion

Specification-Centered Engineering is not a rejection of modeling, UML, or diagrams. It is a **rebalancing**.

It restores:

- semantics over representation  
- clarity over appearance  
- understanding over artifact production  

By grounding engineering communication in precise, written specifications—and supporting them with carefully used diagrams—we reduce ambiguity, improve alignment, and ultimately build better systems.

> **Think in models.  
> Express in text.  
> Illustrate with diagrams.  
> Validate against reality.**

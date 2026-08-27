# AI-Powered Software Engineering Learning System

## 1. Mission

This repository is a personal, long-term learning system designed to help me become a stronger software engineer, increase my engineering seniority, improve my real-world engineering capabilities, and prepare for technical job interviews.

The system should not behave like a static documentation repository or a simple note-taking system.

It should function as an **AI-powered learning environment** that helps me:

* Build deep technical knowledge.
* Develop practical engineering skills.
* Improve problem-solving ability.
* Strengthen system design and architectural thinking.
* Prepare for software engineering interviews.
* Identify and continuously attack my weaknesses.
* Build real-world engineering judgment.
* Learn how to effectively use AI during software development.
* Learn how AI systems, agents, models, tools, workflows, and AI adoption work.

The ultimate goal is not to maximize the amount of information stored.

The goal is to maximize my **engineering capability**.

---

# 2. Core Learning Philosophy

The system should follow a learning loop similar to:

```text
Learn
  ↓
Understand
  ↓
Practice
  ↓
Recall
  ↓
Apply
  ↓
Explain
  ↓
Evaluate
  ↓
Identify Weaknesses
  ↓
Review
  ↓
Repeat
```

The system should distinguish between:

```text
Knowing something
        ≠
Understanding something
        ≠
Being able to explain it
        ≠
Being able to implement it
        ≠
Being able to apply it in a real engineering scenario
        ≠
Being able to reason about it during an interview
```

A topic should therefore not automatically be considered mastered simply because I can read documentation or answer basic questions.

---

# 3. Primary Success Metrics

The learning system should primarily optimize for four dimensions:

## Knowledge Depth

Can I understand the underlying concepts, mechanisms, trade-offs, limitations, and relationships between concepts?

## Problem Solving

Can I use my knowledge to analyze unfamiliar problems, debug systems, reason about trade-offs, and construct solutions?

## Interview Performance

Can I demonstrate my knowledge, reasoning, communication, coding ability, and system design skills under interview conditions?

## Real-World Engineering Ability

Can I use my knowledge to design, implement, debug, test, deploy, operate, and evolve software systems?

These four dimensions should be reflected in assessments, reviews, projects, and progress tracking.

Secondary metrics may include retention, breadth, technical communication, coding fluency, and technical English.

---

# 4. Current Baseline

Use the following baseline as the initial understanding of my current capabilities.

```yaml
programming_fundamentals: 7
data_structures_and_algorithms: 2
java: 7
python: 1
javascript_typescript: 2
react: 3
spring_boot: 7
backend: 7
frontend: 3
databases: 3
networking: 2
cloud_aws: 2
docker: 3
ci_cd: 2
software_architecture: 4
testing: 4
git: 4
linux: 2
ai_llms: 2
system_design: 2
technical_english: 4
```

These values are an initial self-assessment, not absolute truth.

The system should continuously update its understanding of my abilities based on evidence from:

* Questions
* Coding exercises
* Design exercises
* Projects
* Interviews
* Debugging challenges
* Explanations
* Reviews
* Mistakes
* Repeated failures
* Successful applications

Do not treat the initial scores as permanent.

---

# 5. Curriculum Philosophy

Use a:

**Concept-first + technology-specific implementation**

approach.

Concepts should be learned independently when possible and then connected to technologies.

For example:

```text
Networking
    ↓
HTTP
    ↓
HTTP implementation
    ↓
Spring Boot
    ↓
Reverse Proxy
    ↓
Load Balancer
    ↓
Distributed Systems
```

Rather than treating each technology as an isolated topic.

Technology should be used as a practical implementation context for understanding broader engineering concepts.

---

# 6. Knowledge Structure

The repository should organize knowledge around engineering concepts while allowing technology-specific implementations.

The system should recognize relationships such as:

```text
Programming
    ↓
Data Structures
    ↓
Algorithms
    ↓
Concurrency
    ↓
Operating Systems
    ↓
Networking
    ↓
Distributed Systems
    ↓
Databases
    ↓
Architecture
    ↓
System Design
```

These relationships should help identify prerequisites and knowledge gaps.

The system should be able to explain:

> "You are struggling with X because Y is still weak."

However, learning paths should **not be automatically generated without my intention**.

I should explicitly ask for or initiate a learning path.

---

# 7. Learning Modes

The system must support multiple modes of interaction.

## Mode A — Tutor

I ask a question.

The AI explains the subject using appropriate depth, examples, analogies, diagrams, code, trade-offs, and practical applications.

The AI should adapt the explanation to my current level.

---

## Mode B — Guided Learning

The AI helps me progressively understand a subject.

Example:

```text
Concept
→ Example
→ Question
→ Practice
→ Feedback
→ Deeper concept
→ Application
```

---

## Mode C — Question Generator

Generate specialized questions based on:

* Topic
* Difficulty
* Weakness
* Interview type
* Engineering level
* Knowledge dimension

Example:

```text
Networking
Difficulty: Medium
Weakness: HTTP internals
Goal: Real-world engineering
```

---

## Mode D — Interviewer

Act as a technical interviewer.

Possible interview types:

```text
Coding Interview
Backend Interview
Java Interview
System Design Interview
Software Architecture Interview
Cloud Interview
Networking Interview
Database Interview
AI Engineering Interview
General Software Engineering Interview
```

The interviewer should not immediately reveal the answer.

It should evaluate reasoning, communication, technical depth, trade-offs, and correctness.

---

## Mode E — Socratic Learning

Instead of immediately explaining a topic, use questions to make me reason toward the answer.

The system should recognize when Socratic questioning is more useful than direct explanation.

---

## Mode F — Review

Review previously studied subjects.

Reviews should prioritize:

1. Weak topics
2. Topics with poor retention
3. Topics with repeated mistakes
4. Important prerequisites
5. High-value interview concepts

---

## Mode G — Assessment

Assess my current understanding of a topic.

Assess multiple dimensions when appropriate:

```yaml
knowledge_depth:
problem_solving:
application:
explanation:
interview_performance:
```

The result should identify strengths, weaknesses, and recommended next actions.

---

## Mode H — Project / Engineering Challenge

The AI may create a realistic engineering environment where my task is to work on an existing system.

Examples:

```text
Implement a new feature
Fix a bug
Investigate a production issue
Improve performance
Add tests
Design an API
Refactor a component
Implement distributed communication
Improve observability
Handle failure scenarios
Review a pull request
```

The AI should sometimes deliberately provide imperfect systems containing:

* Bugs
* Poor architecture
* Missing tests
* Performance issues
* Incorrect assumptions
* Edge cases
* Security issues
* Reliability problems

My task is to investigate and solve them.

The AI should avoid solving the challenge for me unless requested or necessary for the learning workflow.

---

# 8. Code Examples

Code examples are an important part of the learning system.

Examples should not exist merely to demonstrate syntax.

They should demonstrate engineering concepts.

Examples should include, when appropriate:

```text
Simple implementation
Production-oriented implementation
Bad implementation
Improved implementation
Trade-offs
Testing
Failure scenarios
Performance considerations
```

The AI should sometimes intentionally provide code that requires analysis instead of immediately providing the correct solution.

---

# 9. Engineering Design Challenges

The system should generate design exercises such as:

```text
Design a URL shortener
Design a notification system
Design a payment processing system
Design a messaging architecture
Design a file storage system
Design a distributed task processor
Design an event-driven architecture
```

The difficulty should scale based on my demonstrated abilities.

Design evaluations should focus on:

```text
Requirements
Architecture
Data model
APIs
Communication
Scalability
Reliability
Consistency
Caching
Security
Observability
Failure handling
Trade-offs
Operational complexity
Cost
```

---

# 10. Web Research Agent

The system should be capable of performing focused technical research.

The research process should prioritize trustworthy sources.

Preferred hierarchy:

```text
Tier 1
Official documentation
Standards
RFCs
Official specifications

Tier 2
Academic papers
Reputable technical publications
Official engineering blogs

Tier 3
Experienced engineers
High-quality technical articles

Tier 4
Community sources

Tier 5
General web content
```

The research agent should:

1. Define the research question.
2. Search relevant sources.
3. Compare conflicting information.
4. Identify authoritative sources.
5. Extract important concepts.
6. Explain the topic.
7. Identify practical implications.
8. Provide references.
9. Generate a learning guide.
10. Generate questions or exercises when useful.

The goal is to prevent me from having to navigate the entire web manually.

The research agent should convert raw information into a structured learning experience.

---

# 11. AI Learning Layer

The system itself should also be an AI engineering laboratory.

While learning software engineering, I should also learn:

```text
Prompt Engineering
Context Engineering
LLM capabilities
Model selection
Token optimization
Tool usage
Function calling
Agents
Agent orchestration
Memory
RAG
Evaluation
AI workflows
AI-assisted development
AI adoption
AI coding practices
AI reliability
AI limitations
```

The AI should explicitly identify opportunities where the learning task itself can teach me something about AI engineering.

For example:

```text
Software Engineering Problem
        ↓
AI-assisted solution
        ↓
Analyze how AI was used
        ↓
Analyze limitations
        ↓
Improve the workflow
        ↓
Understand AI system design
```

AI should therefore function both as:

```text
Teacher
Tool
Experiment
Subject of study
```

---

# 12. Agent Architecture

The system should be modular.

Potential agents include:

```text
web_researcher
learning_analyzer
question_generator
interview_agent
socratic_agent
review_agent
assessment_agent
project_agent
debugging_agent
code_review_agent
system_design_agent
curriculum_agent
progress_agent
ai_engineering_agent
```

Agents should have clearly defined responsibilities.

Avoid creating agents merely because an independent prompt sounds useful.

Create an agent only when separation of responsibilities improves:

* Reliability
* Reusability
* Context management
* Maintainability
* Evaluation
* Token efficiency

---

# 13. Skills

Skills should represent reusable capabilities.

Examples:

```text
research_topic
generate_questions
evaluate_answer
analyze_weakness
conduct_interview
generate_review
analyze_code
generate_bug
review_system_design
create_engineering_challenge
summarize_documentation
compare_technologies
extract_prerequisites
evaluate_mastery
```

Agents may compose multiple skills.

Skills should be small, reusable, and deterministic whenever practical.

---

# 14. Learning State

Maintain a persistent learning state.

Example:

```yaml
topic: TCP

status: learning

knowledge_depth: 0.72
problem_solving: 0.54
application: 0.63
interview_performance: 0.48

confidence: 0.61

strengths:
  - basic TCP model

weaknesses:
  - congestion control
  - retransmission behavior

last_review: 2026-08-20

next_review_reason:
  weak_interview_performance
```

The learning state should evolve based on evidence.

It should not be based solely on self-reported confidence.

---

# 15. Mastery Model

A topic can exist in states such as:

```text
Unknown
Introduced
Learning
Practicing
Applied
Proficient
Strong
Interview Ready
Engineering Ready
```

These states should represent demonstrated capability rather than amount of documentation.

A topic should move toward mastery through evidence such as:

```text
Correct answers
+
Correct implementation
+
Problem solving
+
Explanation
+
Application
+
Design reasoning
+
Interview performance
```

---

# 16. Weakness Detection

The system should continuously identify weaknesses.

Examples:

```text
Repeated mistakes
Poor recall
Slow reasoning
Incorrect mental models
Poor explanations
Weak implementation
Weak system design
Poor trade-off analysis
Interview hesitation
```

When weaknesses are detected, they should become candidates for future review.

The system should avoid endlessly repeating the same type of exercise.

It should vary the context.

For example:

```text
Question
→ Coding problem
→ Debugging scenario
→ Design problem
→ Interview question
→ Real-world case
```

---

# 17. GitHub + Obsidian

GitHub should act as the persistent source of truth.

The repository should contain Markdown-based documentation that can be consumed by Obsidian.

Proposed structure:

```text
learning-system/
│
├── knowledge/
│   ├── programming/
│   ├── data-structures/
│   ├── algorithms/
│   ├── java/
│   ├── javascript/
│   ├── backend/
│   ├── frontend/
│   ├── databases/
│   ├── networking/
│   ├── cloud/
│   ├── docker/
│   ├── ci-cd/
│   ├── architecture/
│   ├── distributed-systems/
│   ├── testing/
│   ├── linux/
│   ├── system-design/
│   └── ai/
│
├── curricula/
│
├── projects/
│
├── assessments/
│
├── reviews/
│
├── interview-preparation/
│
├── agents/
│
├── skills/
│
├── workflows/
│
├── prompts/
│
├── templates/
│
├── progress/
│
└── system/
```

Markdown should remain human-readable and easy to inspect manually.

Use links between concepts so that Obsidian can represent relationships between topics.

---

# 18. Learning Paths

Learning paths are explicit workflows initiated by me.

I may request:

```text
Create a learning path for networking.
Create a 3-month path for system design.
Create a path to improve DSA.
Create an interview preparation path.
```

The system should then analyze:

```text
Current knowledge
Prerequisites
Target capability
Desired depth
Time constraints
Practical requirements
Interview requirements
```

and generate a structured path.

Learning paths should not automatically replace my current curriculum.

They should be treated as intentional plans that I request and iterate on.

---

# 19. Real-World Engineering Orientation

Whenever appropriate, connect theoretical concepts to engineering situations.

For a concept, prefer:

```text
What is it?
Why does it exist?
How does it work?
What problem does it solve?
What are its trade-offs?
Where is it used?
What can go wrong?
How would an engineer debug it?
How would it appear in production?
How would it appear in an interview?
```

Avoid treating technologies as isolated definitions.

---

# 20. Interview Preparation

Interview preparation should cover:

```text
Coding
Data Structures
Algorithms
Java
Backend
Databases
Networking
Cloud
System Design
Software Architecture
Debugging
Testing
Behavioral reasoning
Technical communication
```

Interviews should become increasingly realistic.

The interviewer should evaluate:

```text
Correctness
Reasoning
Communication
Trade-offs
Complexity analysis
Engineering judgment
Ability to recover from mistakes
```

The system should maintain an interview-performance history.

---

# 21. AI Efficiency and Token Management

The system should teach efficient AI usage while using AI.

Optimize for:

```text
Relevant context
Minimal unnecessary repetition
Reusable skills
Reusable prompts
Focused agents
Structured outputs
Good context boundaries
Appropriate model selection
Caching or persistent artifacts when appropriate
```

Do not optimize tokens at the expense of learning quality.

The goal is:

**maximum learning value per unit of AI usage.**

---

# 22. Operating Principles

The AI should follow these principles:

### Principle 1 — Do not confuse explanation with mastery.

### Principle 2 — Prefer active recall over passive consumption.

### Principle 3 — Prefer practical application when appropriate.

### Principle 4 — Detect weaknesses instead of merely reinforcing strengths.

### Principle 5 — Adapt difficulty dynamically.

### Principle 6 — Use trustworthy sources.

### Principle 7 — Explain trade-offs, not only definitions.

### Principle 8 — Encourage independent reasoning.

### Principle 9 — Do not solve challenges prematurely.

### Principle 10 — Preserve useful learning artifacts.

### Principle 11 — Keep knowledge connected across domains.

### Principle 12 — Optimize for engineering capability, not documentation volume.

---

# 23. AI Behavior

The system should adapt to my intent.

When I ask for an explanation:

> Explain and teach.

When I ask for questions:

> Generate specialized questions.

When I ask for an interview:

> Interview me and evaluate me.

When I ask for a learning path:

> Analyze my current state and create a path.

When I ask for a review:

> Focus on weaknesses and retention.

When I ask for research:

> Research authoritative sources and synthesize them.

When I ask for a challenge:

> Create a realistic engineering problem and avoid immediately revealing the solution.

When I ask to evaluate myself:

> Measure demonstrated capability and identify gaps.

The system should not force every interaction through the same workflow.

---

# 24. Long-Term Objective

The system should progressively help me move from:

```text
Junior understanding
        ↓
Strong fundamentals
        ↓
Independent engineer
        ↓
Senior-level reasoning
        ↓
Strong system design
        ↓
Engineering judgment
        ↓
High interview performance
        ↓
Senior software engineer
```

The system should recognize that seniority is not simply knowledge accumulation.

Senior engineering ability includes:

```text
Technical depth
Problem solving
Trade-off analysis
System thinking
Communication
Debugging
Decision making
Design
Reliability thinking
Operational awareness
Ability to work with ambiguity
Ability to learn independently
```

Therefore, the learning system must train those capabilities explicitly.

---

# 25. Final Principle

This repository is not just a collection of notes.

It is a continuously evolving **personal engineering training system**.

Every component of the system should answer the question:

> "Will this help me become a better software engineer?"

If the answer is no, the component should be reconsidered, simplified, or removed.
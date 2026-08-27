# Book & Resource Catalog

External learning resources you own, referenced by a stable **id** throughout the system.
Learning paths (`/path`), knowledge notes, and evidence rows cite books by id, e.g. `[[ddia]] ch. 5`.

- The **id** is the filename stem: `resources/files/<id>.pdf` (or `.epub`).
- The actual files are **git-ignored** (kept local); this catalog is the durable, tracked record.
- To read/analyze a book on demand, use the **`book-extract`** skill (page-range extraction via
  `pdftotext`, cached under `resources/extracts/<id>/`). Don't bulk-convert.
- Original filenames are preserved in `resources/filemap.tsv` (also the undo map for the rename).

## Fundamentals & craft

| id | title | topics |
|---|---|---|
| `clean-code` | Clean Code — Robert C. Martin | code-quality, oop |
| `clean-architecture` | Clean Architecture — Robert C. Martin | software-architecture |
| `code-complete-2e` | Code Complete, 2e — Steve McConnell | code-quality, programming-fundamentals |
| `pragmatic-programmer` | The Pragmatic Programmer | code-quality, engineering-judgment |
| `legacy-code` | Working Effectively With Legacy Code — Feathers ⚠️ small file (104 KB) — likely an excerpt | testing, refactoring |
| `swe-at-google` | Software Engineering at Google | software-engineering, culture |
| `soft-skills-sonmez` | Soft Skills: The Software Developer's Life Manual | career, soft-skills |

## Algorithms & data structures

| id | title | topics |
|---|---|---|
| `clrs-3e` | Introduction to Algorithms, 3e (CLRS) | algorithms, data-structures |
| `algorithm-design-manual-2e` | The Algorithm Design Manual, 2e — Skiena | algorithms |
| `grokking-algorithms` | Grokking Algorithms | algorithms, data-structures |
| `algorithms-unplugged` | Algorithms Unplugged | algorithms |
| `algorithms-notes-professionals` | Algorithms Notes for Professionals | algorithms, data-structures |
| `discrete-math-structures` | Discrete Mathematical Structures, 4e | discrete-math |

## Interview preparation

| id | title | topics |
|---|---|---|
| `ctci` | Cracking the Coding Interview | coding-interview, algorithms, data-structures |
| `epi-java` | Elements of Programming Interviews (Java) | coding-interview, algorithms |
| `system-design-interview-xu` | System Design Interview: An Insider's Guide — Alex Xu | system-design |
| `grokking-system-design` | Grokking the System Design Interview | system-design |
| `aspnet-mvc-interview-qa` | ASP.NET MVC Interview Q&A — Chauhan | dotnet, interview |

## Architecture, design & distributed systems

| id | title | topics |
|---|---|---|
| `ddia` | Designing Data-Intensive Applications — Kleppmann | distributed-systems, databases, system-design |
| `poeaa` | Patterns of Enterprise Application Architecture — Fowler | software-architecture |
| `head-first-design-patterns` | Head First Design Patterns | design-patterns, oop |
| `building-microservices-1e` | Building Microservices, 1e — Newman | microservices, distributed-systems |
| `building-microservices-2e` | Building Microservices, 2e — Newman | microservices, distributed-systems |
| `systems-analysis-design-9e` | Systems Analysis and Design, 9e | software-engineering |

## Databases

| id | title | topics |
|---|---|---|
| `fundamentals-database-systems-6e` | Fundamentals of Database Systems, 6e | databases |
| `concise-guide-databases` | A Concise Guide to Databases | databases |
| `postgres-notes-professionals` | PostgreSQL Notes for Professionals | databases, postgres |
| `mssql-notes-professionals` | Microsoft SQL Server Notes for Professionals | databases, sql-server |
| `ef-notes-professionals` | Entity Framework Notes for Professionals | databases, dotnet |

## Networking & security

| id | title | topics |
|---|---|---|
| `forouzan-data-comm-networking` | Data Communications and Networking — Forouzan | networking |
| `advanced-network-programming` | Advanced Network Programming: Principles & Techniques | networking |
| `data-analysis-network-security` | Data Analysis for Network Cyber-Security | security, networking |
| `writing-secure-code-2e` | Writing Secure Code, 2e | security |

## Java

| id | title | topics |
|---|---|---|
| `intro-java-programming-10e` | Introduction to Java Programming, 10e — Liang | java, programming-fundamentals |

## .NET / C#

| id | title | topics |
|---|---|---|
| `csharp-5-nutshell` | C# 5.0 in a Nutshell | csharp |
| `csharp-notes-professionals` | C# Notes for Professionals | csharp |
| `csharp7-netcore-blueprints` | C# 7 and .NET Core 2.0 Blueprints | csharp, dotnet |
| `oop-in-csharp-4e` | Object-Oriented Programming, 4e ⚠️ verify language (C#/C++) | oop |
| `dotnet-book-zero` | .NET Book Zero — Charles Petzold | dotnet, csharp |
| `architecting-modern-web-aspnet` | Architecting Modern Web Apps with ASP.NET Core & Azure | dotnet, web, cloud |

## Frontend / Angular

| id | title | topics |
|---|---|---|
| `pro-angular-9` | Pro Angular 9 | angular, frontend |
| `ng-book-angular8` | ng-book: The Complete Guide on Angular 8 | angular, frontend |
| `pwa-with-angular` | Progressive Web Apps with Angular | angular, frontend, pwa |
| `aspnet-core3-angular9` | ASP.NET Core 3 and Angular 9 — De Sanctis | dotnet, angular, fullstack |

## AI / ML / Data science

| id | title | topics |
|---|---|---|
| `aima-3e` | Artificial Intelligence: A Modern Approach, 3e | ai |
| `hands-on-ml-2e` | Hands-On Machine Learning (Scikit-Learn, Keras, TF), 2e — Géron | ml |
| `ml-for-coders` | AI and Machine Learning for Coders | ml |
| `ml-algorithms-2e` | Machine Learning Algorithms, 2e | ml |
| `mastering-ml-algorithms-2e` | Mastering Machine Learning Algorithms, 2e (EPUB) | ml |
| `ai-by-example` | Artificial Intelligence By Example | ai, ml |
| `bayesian-reasoning-ml` | Bayesian Reasoning and Machine Learning — Barber | ml, statistics |
| `hands-on-data-science` | Hands-On Data Science | data-science |
| `opencv4-python-blueprints` | OpenCV 4 with Python Blueprints | computer-vision, python |

## Language references (quick lookups)

| id | title | topics |
|---|---|---|
| `python-notes-professionals` | Python Notes for Professionals | python |

> ⚠️ flags: `legacy-code` looks like an excerpt (very small); `oop-in-csharp-4e` — confirm whether
> it's C# or C++ before citing precisely. Update this catalog as you verify or add resources.

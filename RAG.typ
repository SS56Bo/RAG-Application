#set text(
  font: "Arial",
  size: 10pt
)
= What is RAG ?
\
RAG stands for Retrieval Augmented Generation.

The goal of RAG is to take information and pass it to an LLM so it can generate output based on that information.

- #text(weight: "bold")[Retrieval] - Find relevant information given a query 
- #text(weight: "bold")[Augmented] - We want to take relevant information and augment our output (prompt) to an LLM with that relevant information.
- #text(weight: "bold")[Generation] - Takes the first two steps and pass them onto the LLM for output generation.

= Why RAG ?
\
The main goal of RAG is to improve the generation outputs of LLMs.\

Disadvatages of RAG:
1. #text(weight: "bold")[Prevent hallucination] - LLMs are incredibly good at generating text, these texts while good-looking, does not gaurantee that it's factually correct.
2. #text(weight: "bold")[Custom Data] - Since LLM are mainly trained with scaled data. This means they have a fairly good idea of language command, however they often fail when approached with custom questions. #text(weight: "extrabold")[RAG helps in generating specific responses to specific documents.]


= What can be RAG used for ?
\
- #text(weight: "bold")[Customer Support Q&A Chat] - Helps in finding out specific parts from a document, and help the customer. #text(weight: "bold")[Retrieval systems can be used to retrieve relevant documents and answer queries accordingly].
- #text(weight: "bold")[Email Chain Analysis] - Use to find relevant information from a chain of emails, it is used to find relevant information from these emails and then can be used in LLMs to find structured outputs and information.
- #text(weight: "bold")[Textbook Q&A] - Can be used to synthesize information from books, which can be in term fed to an LLM for further processing.

= Why run locally ?
\
Privacy, speed, cost.

- #text(weight: "extrabold")[Privacy] - Since most RAG models run using API, sending privacy-sensitive documents become a concern of privacy. 
- #text(weight: "extrabold")[Speed] - Sending to a RAG API, answers that are recieved might be slow. Running locally means we will not have to for transfers of data. 
- #text(weight: "extrabold")[Cost] - If you own your hardware, the cost is paid. Also, won't have to pay vendors cause it's our very own service.

= Approach
\
- #text(weight: "extrabold")[Format the text in the PDF to ready it for embedding models.]
- #text(weight: "extrabold")[Process the chunks of data and convert them into numerical values (embedding).]
- #text(weight: "extrabold")[Build a Retrieval system that uses vector search to find relevant chunk of text based on query.]
- #text(weight: "extrabold")[Create prompts that incorporate the retrieved pieces of text.]
- #text(weight: "extrabold")[Generate an answer to a query based on text retrieved from the PDF using an LLM.]

= Key Terms
\
#table(
  columns: (auto, auto),
  inset: 10pt,
  align: horizon,
  table.header([*Term*], [*Description*]),
  $"Token"$,
  [
    A sub-word piece of text. A token can be a whole word, part of a word or a group of punctuation characters. \
    #text(weight: "bold")[Texts get broken into parts before being passed into an LLM.]
  ],
  $"Embedding"$,
  [],
  $"LLM Context Window"$,
  [
    The number of tokens a LLM can accept as input. A higher context Window means an LLM can accept more relevant information to assist with a query. In RAG systems, if a model has a larger context Window, it can accept more reference items from the retrieval system to aid with its generation.
  ]
)


= Why is token count important ?
\
Token Count is important to consider as most LLMs cannot deal with infinite tokens. Some tokens only embed less than 360 tokens. 
The more tokens, the more memory and computation required. In some LLMs, token count determines sequence length for models like Transformers, RNNs, etc.

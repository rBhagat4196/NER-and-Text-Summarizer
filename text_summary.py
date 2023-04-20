from heapq import nlargest
import spacy
from spacy import displacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text = """A programming language is a system of notation for writing computer programs.[1] Most programming languages are text-based formal languages, but they may also be graphical. They are a kind of computer language.

The description of a programming language is usually split into the two components of syntax (form) and semantics (meaning), which are usually defined by a formal language. Some languages are defined by a specification document (for example, the C programming language is specified by an ISO Standard) while other languages (such as Perl) have a dominant implementation that is treated as a reference. Some languages have both, with the basic language defined by a standard and extensions taken from the dominant implementation being common.

Programming language theory is the subfield of computer science that studies the design, implementation, analysis, characterization, and classification of programming languages."""

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    # print(stopwords)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    # print(doc)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    html = displacy.render(doc,style="ent")

    word_freq = {}
    for word in doc :
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    
    # print(word_freq)

    max_freq = max(word_freq.values())
    print(max_freq)

    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq

    # print(word_freq)

    sent_tokens = [sent for sent in doc.sents]

    # print(sent_tokens)

    sent_scores = {}

    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                  sent_scores[sent] = word_freq[word.text]
                else:
                  sent_scores[sent] += word_freq[word.text]

    # print(sent_scores)
    percent = 25;
    percent = percent/100;
    select_len = int(len(sent_tokens)*percent)
    # print(select_len)

    summary = nlargest(select_len , sent_scores , key = sent_scores.get)
    # print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    # print(text)
    # print(summary)

    # print("Length of original text " , len(text.split(' ')))
    # print("Length of summary text " , len(summary.split(' ')))
    # orig_text = rawdocs
    return summary , doc, len(rawdocs.split(' ')) , len(summary.split(' ')) , entities , html


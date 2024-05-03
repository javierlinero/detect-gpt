import openai
import numpy as np

def main(text):
    openai.api_key = "put token here"
    response = openai.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    messages=[
                        {"role": "user", "content": f"Repeat the following text and extend it: {text}"}
                    ],
                    max_tokens=200,
                    logprobs=True,  # request log probabilities
                    temperature=0
                )

    choice = response.choices[0]
    tokens = [token.token for token in choice.logprobs.content]
    token_logprobs = [token.logprob for token in choice.logprobs.content]

    print(tokens)

    if token_logprobs:
        print(np.mean(token_logprobs))

if __name__ == "__main__":
    hello = "The problem is as in the title, assume"
    main(hello)
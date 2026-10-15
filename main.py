from services.llm_service import LLMService


def main():
    llm = LLMService()

    response = llm.generate(
        "Explique o que é uma API REST em até três frases."
    )

    print(response)


if __name__ == "__main__":
    main()
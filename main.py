from services.llm_service import LLMService


def main():
    llm = LLMService()
    history = []

    print("Assistente de Conhecimento")
    print("Digite 'sair' para encerrar.\n")

    while True:
        question = input("Você: ").strip()

        if question.lower() == "sair":
            print("Encerrando o assistente.")
            break

        if not question:
            continue

        history.append({
            "role": "user",
            "content": question,
        })

        response = llm.generate(history)

        history.append({
            "role": "model",
            "content": response,
        })

        print(f"\nAssistente: {response}\n")


if __name__ == "__main__":
    main()
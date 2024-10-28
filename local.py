

import ollama

response = ollama.chat(

    model="llama3.2:1b",
    messages=[
        {
            'role': 'system',
            'content': 'You are o1, an AI assistant focused on clear step-by-step \
                reasoning. Break every task into 4 actionable \
                    steps.Always answer in short.'


        },
        {
            'role':'user',
            'content': 'i want to lose weight and your \
                task is to design a 7-day workout plan that \
                im gonna follow every weekday.'
        }
    ]

)

print(response['message']['content'])   


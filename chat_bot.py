from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatebot',read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])
# bot = ChatBot('chatebot', read_only=False, tagger_language=None, logic_adapters=["chatterbot.logic.BestMatch"])

# Create list trainer
list_trainer = ListTrainer(bot)


list_to_train = [
    "I feel anxious all the time. What can I do?",  
    "Can you suggest a breathing exercise for panic attacks?",  
    "How do I know if I need therapy?",  
    "I’m having trouble sleeping. Any tips?",  
    "What are some free yoga routines for stress?",  
    "I feel overwhelmed with work. Help?",  
    "Are there support groups for depression?",  
    "What’s mindfulness, and how does it help?",  
    "I’m having suicidal thoughts. What should I do?",  
    "Can you recommend a CBT technique for anger?",  
    "How do I talk to a friend about my anxiety?",  
    "What foods improve mental health?",  
    "I’m lonely. Any advice?",  
    "How do I practice gratitude daily?",  
    "What’s the 4-7-8 breathing method?",  
    "Can exercise really reduce depression?",  
    "I need a distraction from negative thoughts. Ideas?",  
    "What’s the best way to journal for mental health?",  
    "How do I set boundaries to reduce stress?",  
    "Are there apps for guided meditation?",  
    "What should I do if my anxiety feels unmanageable?",  
    "How can I help a loved one with bipolar disorder?",  
    "What are early signs of burnout?",  
    "Can you explain cognitive distortions?",  
    "I’m struggling to focus. Any ADHD tips?",

    # New Questions: Anxiety (25 additional)
    "How can I manage my anxiety at work?",
    "What are some quick ways to calm down during a panic attack?",
    "Are there any natural remedies for anxiety?",
    "How can I tell if my anxiety is normal or if I need help?",
    "What should I do if I feel anxious in social situations?",
    "How do I stop overthinking everything?",
    "Can you suggest a relaxation technique for anxiety?",
    "Hey, I’m feeling really anxious. Any tips?",
    "What’s a good way to handle anxiety before a big event?",
    "Are there exercises to reduce anxiety quickly?",
    "How can I calm my mind when it’s racing?",
    "What if my anxiety keeps me up at night?",
    "Can anxiety cause physical symptoms?",
    "How do I deal with anxiety about the future?",
    "What’s the best way to breathe when I’m anxious?",
    "Are there apps that help with anxiety?",
    "How can I stop worrying about things I can’t control?",
    "What should I say to a doctor about my anxiety?",
    "Can you tell me more about anxiety disorders?",
    "How do I handle anxiety in a crowded place?",
    "What’s a simple trick to feel less anxious?",
    "How can I support my partner with anxiety?",
    "Is anxiety worse in the morning?",
    "What’s the difference between stress and anxiety?",
    "How do I relax when I’m feeling on edge?",

    # New Questions: Depression (15 additional)
    "What are the symptoms of depression?",
    "How can I support a friend who is depressed?",
    "Are there any lifestyle changes that can help with depression?",
    "What should I do if I think I might be depressed?",
    "How can I find a therapist for depression?",
    "Is there a difference between sadness and depression?",
    "What are some coping strategies for seasonal depression?",
    "How do I deal with feelings of hopelessness?",
    "Can you suggest something to do when I feel down?",
    "How do I get out of bed when I’m depressed?",
    "What’s a small step to feel better when I’m depressed?",
    "Are there online resources for depression?",
    "How can I tell if my depression is getting worse?",
    "What if I don’t feel like talking to anyone?",
    "How do I help my teenager with depression?",

    # New Questions: Therapy (10 additional)
    "What are the benefits of therapy?",
    "How do I find a therapist that’s right for me?",
    "What can I expect in my first therapy session?",
    "Is online therapy as good as in-person?",
    "How much does therapy usually cost?",
    "Are there free therapy options available?",
    "What types of therapy help with anxiety?",
    "How do I know if therapy is helping me?",
    "Can you tell me about cognitive behavioral therapy?",
    "What’s exposure therapy, and does it work?",

    # New Questions: Mindfulness (10 additional)
    "How does mindfulness help mental health?",
    "What are some easy mindfulness exercises?",
    "How can I be mindful if I’m always busy?",
    "Is meditation the same as mindfulness?",
    "Can mindfulness help me stay calm?",
    "How do I start meditating every day?",
    "What’s a good mindfulness app?",
    "How does mindfulness reduce stress?",
    "Can mindfulness improve my concentration?",
    "What’s a quick mindfulness trick for tough moments?",

    # New Questions: Exercise (10 additional)
    "How can exercise improve my mood?",
    "What exercises are best for anxiety?",
    "Can yoga help with depression?",
    "How often should I exercise for mental health?",
    "What’s a simple home workout for stress?",
    "Does walking really help my mind?",
    "How does exercise affect my mood?",
    "Can exercise replace therapy or meds?",
    "What stretches help me relax?",
    "How do I stay active when I feel low?",

    # New Questions: Nutrition (10 additional)
    "What foods can reduce anxiety?",
    "Are there diets that help depression?",
    "How does food affect my mental health?",
    "What are some mood-boosting snacks?",
    "Does coffee make anxiety worse?",
    "Is sugar bad for depression?",
    "What supplements help mental health?",
    "Does drinking water improve my mood?",
    "What foods help me focus better?",
    "What’s the best diet for my brain?",

    # New Questions: Loneliness & Social Connection (10 additional)
    "How can I stop feeling so lonely?",
    "What’s a good way to meet new people?",
    "How do I handle being alone too much?",
    "Can pets help me feel less lonely?",
    "Why do I feel lonely even with people around?",
    "How do I connect with others when I’m down?",
    "Are there online groups for mental health?",
    "How do I reach out when I feel alone?",
    "What solo activities help with loneliness?",
    "How can I help a lonely friend?",

    # New Questions: General Mental Health (25 additional)
    "How can I keep my mental health strong?",
    "What are signs I need professional help?",
    "Can you explain what burnout feels like?",
    "How do I cope with anger issues?",
    "What’s a good habit for mental well-being?",
    "How can I deal with guilt?",
    "What are some self-care ideas?",
    "How do I handle bad days?",
    "Can you suggest a stress-relief activity?",
    "What’s the benefit of positive thinking?",
    "How do I talk about my mental health?",
    "What if I’m scared to get help?",
    "How can I boost my confidence?",
    "What’s a good way to unwind?",
    "How do I stop feeling so tired all the time?",
    "Can you tell me about PTSD?",
    "What’s obsessive-compulsive disorder like?",
    "How do I deal with grief?",
    "What are some calming nighttime routines?",
    "How can I manage work-life balance?",
    "What’s a sign of good mental health?",
    "How do I help a kid with stress?",
    "What’s the best way to ask for support?",
    "How can I feel less overwhelmed?",
    "What should I do if I’m feeling lost?"
]

list_tranier = ListTrainer(bot)

# list_tranier.train()
list_trainer.train(list_to_train)
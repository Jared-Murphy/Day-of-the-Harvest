# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The persistent variable saves as a variable in the game. Currently 

define e = Character("questionaire")
define n = Character("Narrator")
define c = Character("Collector")
define tc = Character("The Collectors")
define cogM = Character("Cog(Male)")
define cogF = Character("Cog(female)")
define fm = Character("Floor Manager")
define Craig = Character("Craig")
define hm = Character("homeless man")
define meli = Character("Melissa (Wife)")
define ceo = Character("CEO")
define Waste = Character("Waste")

define Phone = Character("Phone")
define Driver = Character("Driver")
define Skittles = Character("Skittles the Cat")





define persistent.gameDone = None

#cog story path variables
default refund = False
default system = False
default cannot = False
default haveTo = False


# The game starts here. This block of text plays before the game starts to provide a content warning to the user of mature content 
label splashscreen:
    scene black
    with Pause(1)

    show text "Content Warning: \n Game contains themes of blood, gore and corruption." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

return

#this is when you press start on the main menu. It'll set assets such as characters, backgrounds, UI elements. 

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image bg room = im.Scale("room.jpg", 2000, 1200)
    image bg darkalley = im.Scale("darkalley.jpg", 2000, 1200)
    image bg streets = im.Scale("streets.jpg", 2000, 1200)
    image bg office = im.Scale("office.jpg", 2000, 1200)
    image bg room = im.Scale("room.jpg", 2000, 1200)
    scene bg room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "CEO.png" to the images
    # directory.
    # A score counter is changed by the players based on the choices they make. Based on the amount of points 
    # the player will experience differnt stories 

    image questionaire = im.Scale("questionaire.png", 1000, 1000)
    show questionaire 
    $ score_counter = 0

    # Questionaire starts here. 

    e "Before we continue, please answer the questionaire. This will help us know whether you can survive in this world."
    e "Your final score will determine where you will find yourself in society."

    e "What matters most in this world?"
    menu:

        "My Happiness":
            $ score_counter += 1

        "My comfort":
            $ score_counter -= 1

        "Profit":
            $ score_counter += 2

        "Survival":
            $ score_counter += 1
    
    e "What would you sacrafice to succeed?"
    menu:

        "Happiness":
            $ score_counter 

        "Comfort":
            $ score_counter -= 1

        "My Morals":
            $ score_counter += 1

        "Everything":
            $ score_counter += 2

    
    e "You hold your daughter in your arms. She's so tiny. Her little fingers wrap around your pinkie. 
    She laughs, and her wide black eyes fix on yours. There is not a single thought of sadness in that tiny newborn."
    e "She is so gentle. What do you do?"
    menu:

        "Cherish the moment":
            $ score_counter -= 1

        "Get back to work":
            $ score_counter += 1

    e "A homeless man is lying face down on the ground in front of you. He isn't moving. What do you do?"
    menu:

        "Keep walking":
            $ score_counter += 0


        "Make sure he's okay":
            $ score_counter -= 1
        
        "Put money in his cup":
            $ score_counter -= 2

        "Stomp on him.":
            $ score_counter += 2

    e "Do you hate yourself?"
    menu:

        "Of course i do.":
            $ score_counter += 1

        "Who could possibly love a waste of space?":
            $ score_counter += 1
        
        "I am happy with myself":
            $ score_counter -= 1

        "There is nothing to hate. I am nobody":
            $ score_counter += 2
    
    e "Your daughter is asking you to come play with her. You are finally home after so much time at work, all that overtime. "
    e "She's got a little dirt on her face, but she's beaming."
    e "Daddy, can't you come outside? You look down from your computer. Scrolling text. It's an important deal you've been working on - something that might get you a big promotion if it works. "
    e "But you haven't seen much of your daughter in weeks, you were so busy with the last big deal."
    e "She is smiling. Gleaming brown eyes. Missing front tooth."
    menu:

        "The work can wait. Play with your daughter.":
            $ score_counter -= 1

        "Your daughter will have to wait. This is important.":
            $ score_counter += 1

    e "What is your body?"
    menu:

        "A weakness":
            $ score_counter += 1

        "A part of me.":
            $ score_counter -= 1

        "A parasite that wastes my money.":
            $ score_counter += 2

        "A means to an end":
            $ score_counter += 1
    
    e "What is free time?"
    menu:

        "A sign that I'm not doing enough":
            $ score_counter += 1

        "A moment for reflection.":
            $ score_counter -= 1

        "A time to spend with loved ones":
            $ score_counter -= 2

    e "Your daughter is looking at you from above. 
    You lie in the bed.
    The machine beeps."
    e "She is crying.
    But glaring.
    You have not spoken in years. "
    e" She has grown into a beautiful woman.
    And she has grown to hate you."
    e"You were never there for her.
    Always working, always busy."
    e"When her mother died, you were working.
    When she got married, you were working."
    e"When her first child was born, you were working.
    She is waiting for something."

    e"You don't have long.
    What do you say to her?"
    menu:

        "I'm sorry":
            $ score_counter -= 1

        "I don't say anything at all.":
            $ score_counter += 1

    #first choice with options. Everytime you choose a different option we use flags and labels to show where we want to jump into the story
    #this will be the default way of jumping between stories, and choices that have different text. 
    e "Your childhood toy, Bingo. Head of a soft teddy bear with a body made of a blanket. White fluff turned beige by time. Rip in the corner. Old, but you remember him now. "
    menu:

        "Remember the past":
            $ score_counter -= 1
            jump bingo_bad_flag
            

        "Throw it away.":
            $ score_counter += 1
            jump bingo_good_flag
    
    #bad option jumps
    label bingo_bad_flag:

            e "You remember the times you slept with Bingo, how you used to suck your thumb but your parents told you that you would need braces if you kept doing that, so you held on really close to Bingo to make sure your hand didn't go to your mouth when you slept. "
            menu:
                
                "A soft smile forms on your lips.":
                    $ score_counter -= 3
                    jump bingo_verybad_flag
                
                "You are disgusted":
                    $ score_counter += 1 
                    jump bingo_smart_flag
    
    label bingo_verybad_flag:

            e "You think of more memories. Of running through the cul-de-sac with the others. What were their names? Back when the sky was blue, when there was a horizon. What were their names?"
            menu:
                
                "Try to remember.":
                    $ score_counter -= 3
                    jump bingo_yikes_flag
                
                "It doesn't matter. They are in the past. The future is all that matters.":
                    $ score_counter += 1 
                    jump Bingo_recovered_flag

    

    label bingo_yikes_flag:
            e "They might as well all be dead for all they matter. 
            Then again, seeing as you did this, you are no different."
        
            $ score_counter -= 5
            jump Questionaire_over

    label Bingo_recovered_flag:
            e "Correct."
            $score_counter += 1
            jump Questionaire_over

    
    #good option jumps
    label bingo_good_flag: 
            e "You toss it in the trash and let the lid slam. It's gone, it's trash now. It's where it belongs. What do you feel?"
            menu:
                "Regret.":
                    $ score_counter -= 3
                    jump bingo_tried_flag
                
                "Absolutely nothing.":
                    $ score_counter += 1
                    jump bingo_smart_flag


    label bingo_smart_flag:
            e "Perhaps you aren't as stupid as you look"
            jump Questionaire_over

    label bingo_tried_flag:
    
            e "You were doing so well. But it appears you don't really have the mindset."
            menu:
                "I'm sorry.":
                    $ score_counter -= 5
                    jump bingo_shame_flag
                
                "I have it. This was a moment of weakness":
                    $ score_counter += 1 
                    jump Bingo_salvaged_flag

                "I guess not...":
                    $ score_counter -= 5
                    jump bingo_shame_flag
    
    label bingo_shame_flag:
        e "That's a shame"
        jump Questionaire_over


    label bingo_salvaged_flag:
        e "It better be. For your sake"
        jump Questionaire_over


    # all bingo routes lead to questionaire end. Currently if ceo story is not accessible if the user has not triggered persistetnt flag. 
    # Persistent flag is triggered when the game ends and the appopriate text will play when finished. 
    label Questionaire_over:
        hide questionaire with dissolve
        e "Your score is [score_counter]"

        if score_counter <= 0:
            jump waste_story
        if score_counter <= 8:
            jump cog_story
        if score_counter < 17:
            jump business_story
        if score_counter >= 16 and persistent.gameDone:
            jump ceo_story

#Put stuff for waste story here 
    label waste_story:
        #put text here for the story until waste road choice
        n "You are homeless."
        
        n "You have been for weeks…or was it months…years? It’s hard to tell now."
        
        n "Your family is gone. Taken. You are alone."
        
        n "You are waking up. Just another day."

        
        
        #Introduce alleyway asset. Add the homeless man/woman asset based on the chosen gender variable
        scene bg alleyway
        with fade

        n "A sigh escapes your chapped and bloody lips. The black, smokey sky once again fills your eyes, nose, and lungs. That constant backdrop is part of the reason why it’s so hard to tell when days pass on."
        
        n "What’s left of them, anyway. What isn’t entirely broken from decades of labor."
        
        n "The skyscrapers that surround the alleyway in which you slept in aren’t much better. They’re only a slight tint brighter than what was above, and so tall as to reach nearly as high."
        
        n "It’s a miracle you even found this place. It's a miracle alleyways still exist now that you think about it."
        
        n "You slept more than usual, you believe. You knew you couldn’t afford to, but the desire to doze overcame any other thought. Luck overcame there too."
        
        n "After all, it’s awfully hard to rest most nights to avoid being taken for The Harvest."
        
        n "You think it’s soon, at least. The ‘engine of progress’ has gotten quieter. Not like that matters to you any more."
        
        n "The surrounding buildings churned less and less and temporarily got rid of the racket that pounded in your ears."
        
        n "In that way, today actually started off pretty well all things considered."
        
        n "A cough of blood escapes your feeble form."
        
        n "All things considered…"
        
        n "Still…you can’t just give up hope. These better circumstances mean there’s something to keep going for…"
        
        n "Right?"

        menu: 
            "Give up":
                jump waste_giveUp

            "Continue on":
                jump waste_continueOn
                    
    label waste_giveUp:
    
        n "The more you think about it, the less reason there is to keep hope."
    
        n "What good did it give you? What good did it give your family? What good did it give to everything you cared for?"
    
        n "You hoped too much."
    
        n "That’s why it’s all gone."
    
        n "It always ends up that way sooner or later."
    
        n "The only question is the agency of it: do you give it up or does the world take it?"
    
        n "For you it was the latter."
    
        n "As often as they told you to get them out of your mind, as often as they told you that they meant nothing, your conscience couldn’t allow it. You hoped you would thrive despite that."
    
        n "They didn’t allow it."
    
        n "So here you are in an alleyway you’d probably have to leave soon. Here you are having to scrounge for scraps. Here you are. What was the point?"
    
        n "There wasn’t one. They were sure to beat that into your skull. Only now is it just getting through."

        #Adjust scene to streets asset
        scene bg streets
        with fade
    
        n "You look out into the trash filled streets as what little color you had left leaves your body. Your body died long ago. Your mind is coming with it."
    
        n "In those brief moments, you continue to wonder…what was the point of the Harvest?"
    
        n "Those brief moments before you notice someone standing across from you on the street."
    
        #Add/apply giveUp variable to be used in the waste_end section
    
        jump waste_end



    label waste_continueOn:
    
        n "Right. You didn’t come this far just to give up now. To just break after all these years."
    
        n "What would your family have thought if you did that? No, you have to keep going."
    
        n "After a few stretches of your tired muscles (or lack thereof), you walk out of your temporary home. No use just thinking about hope. You had to get food."
    
        #Adjust scene to streets asset
        scene bg streets
        with fade
        n "The streets were just as dark as the skyscrapers and sky – nothing new. Nor were the neon signs you long since avoided glancing at. Nor were the more appealing colors of trash that litter the cracked sidewalks."
    
        n "Once again aside from these meager surroundings, you were alone. Anyone employed surely wouldn’t risk their safety to walk or even drive. Why would they when the subways take a direct line to their designated homes and workplace?"
    
        n "Any other hobos around are sure to hide out in their own filth holes to stay out of sight. Either that or stay on the move hunting in trash piles further along the street. Anything to not be caught with ease."
    
        n "Your legs buckle for a moment as you walk out and bid your temporary quarters farewell. Well, after you make sure your locket is still with you."
    
        n "Your last physical trace of your family aside from your own biological components."
    
        n "One more cough of blood and you’re off."
    
        #Cut to black
    
        #Maybe adjust this from narrator to blank
        n "Hours later…"
    
        #Cut back to streets asset, littered with trash assets, and the main character homeless man/woman asset
    
        n "Nothing. Still nothing. No matter how much you scrounge for food today, the trash piles seemed to house no viable sustenance."
    
        n "The key word was viable. There was no way you were taking food from the few occasional hobos you saw as you passed by. The ones who already found some in piles they searched."
    
        n "You knew life was hard enough to resort to such methods…even if the executives probably would’ve encouraged it."
    
        n "A shudder courses through your body and even into your cybernetics at just the thought of it. Best not to think about that."
    
        n "You begin looking through another pile, dirt and grime continuing to latch onto your hands. And then…you see it."
    
        n "A sandwich! A nearly whole cheese sandwich in a plastic bag!"
    
        n "Briefly wiping your hands and mouth to have some sort of cleanliness you tore open the bag, and held the carb filled deliciousness up in the air. Your jaws open wide, ready to snap shut in an instant…"
    
        n "…that is until you see her."
    
        #Adjust scene by adding homeless woman asset, ideally looking different or at least with different clothes compared to the normal homeless woman asset
    
        n "Another homeless and unemployed just like you. Unlike the others of today though, she stares back. You pause to look her over."
    
        n "She’s even more gaunt than you. She’s missing an entire arm. She’s desperate, even without words."
    
        #menu option to share the sandwich 
        n "Do you share the sandwich?"
    
        menu: 
                "Yes":
                    jump waste_shareFood

                "No":
                    jump waste_dontShareFood

    label waste_shareFood:
    
        #Add/apply helpOthers variable
        
        n "You split the sandwich in two before handing one half to her. After nearly a minute, she reaches her remaining arm out and holds it, taking a bite."
        
        #Adjust scene to get rid of homeless woman asset
        
        n "She walks away without a word spoken. Despite that, you smile."
        
        n "Because you saw her smile."
        
        n "This is hope."
        
        n "You lie down using the pile as support. Today was a good day."
        
        n "It lasts for quite a while…but then reality sets in. You finally hear other homeless people’s clatter."
        
        n "You lift your head up from the pile."
        
        jump waste_end

    label waste_dontShareFood:
        
        n "As much as it pains you…as much as you hate yourself for it…as much as it continues to remind you of those higher above you…"
        
        n "You can’t do it."
        
        n "You give her a somber expression before looking away and taking a bite."
        
        #Adjust scene to get rid of homeless woman asset
        
        n "By the time you finished eating and you looked back, she was gone."
        
        n "It’s a mistake. You know it is."
        
        n "You huddle your body next to the pile. You cry."
        
        n "You don’t know for how long. Nothing new."
        
        n "By the time you look up, you see them."
        
        jump waste_end

    label waste_end:
        #default ending for all routes regarding "the waste path"

        n "A man is staring at you."
        
        n "A man wearing the traditional garb of collectors."

        n "Shit." 
        
        n "He looks terrified, he's covered in sweat, but he's still coming closer. Must have been a new recruit, and a lowly one at that. Only they still had morals enough to outwardly show regret."
        
        n "To show regret before forcing people into the Harvest. Nonetheless, behind his expression you could see it."
        
        n "The inner fire to rise up the ranks has been stoked substantially. He won’t stop himself."
        
        #Need some way to include giveUp variable and corresponding text and panning across screen.
        
        n "You run."
        
        n "It's the day of the harvest, and you're unemployed."
        
        n "Bad day all things considered."

        n "The man is running now." 
        
        c "Stop! Listen to me!"
        
        n "You run faster. All around you, signs with WORK and EMBRACE DISCIPLINE blur together."

        n "You trip over a discarded bottle. The man's hands are on you within seconds. He wraps his arm around your throat and whispers"
        
        c "I'm so sorry" 
        
        n "...Just before the needle plunges into your neck. You black out."
        
        #Include the scene addition as is described in the google doc for this path

        n "You come to with dozens of others in a dark space. Based on the shaking and the noise, it must be a truck. Your wrists are bound behind your back, the cord digs into your skin. Your feet are bound too, but not enough to stop you from moving - just enough to make it so you can't run."
        
        n "The people are sobbing. Men, women, children. The few who aren't crying are either asleep or barely choking down their whimpers."
        
        #Including text from the helpOthers variable as put in a comment before
        
        n "You all know exactly what's coming."

        n "The Harvest."
        
        #Add several “The Cog” character assets in Harvest uniforms

        n "The collectors drag you out, grimacing behind their sunglasses as you are brought into the sound of slow, deep sputtering. An engine with no fuel. You want to appear strong."
        
        n "But you know what's coming." 
        
        n "Just look at you. There's no chance that putting on a show now will impress them.
        Even with the sky blocked by smog, your eyes take a few seconds to adjust."

        tc "The market requires blood."
        
        #Adjust scene to The Pit asset. Get rid of all but one of “The Cog” character assets in Harvest uniform

        n "The pit is enormous. A huge circle of concrete overlooking a deep hole, its sides stained increasingly dark shades of brown."
        
        n "Lines of black trucks pass between a massive wall of skyscrapers that overlook this place. How many have they brought for this Harvest?"
        
        n "At its center is a massive, incomprehensible machine. Blackened metal, enormous smokestacks, tubes leading nowhere and a dull red glow emanating from it."
        
        n "Sharp spikes and needles spin across its surface in lazy orbits, chains made of spindles. Each booming sputter of the engine of progress as it struggles to run sounds like the beat of a vast heart. "
        
        n "The man marches you to the lip of the pit and kicks the back of your leg."
        
        n "You barely feel it as you fall to your knees. Your eyes are locked on the great engine."
        
        n "A hand presses your head into place, your throat now right against the rim of the pit."
    
        n "No need to scream now. You know what's coming."

        n "You feel the blade glide into your throat."
        
        #Adjust screen to be red tinted, either with a slightly adjusted Pit asset, or a not fully opaque red overlay. Not sure which would be easier.
        
        n "The world falls quiet except for the sound of your heart beating out pulse after pulse of your blood across the wall of the pit."
        
        n "So much red, moving so quickly down the wall."
        
        n "The engine pulses in time with your heart."
        
        n "Even as it slows."
        
        n "The market grows stronger."
        jump the_end

        
    #cog story
    label cog_story:
        scene bg office
        with fade
        n "You are [Name], a clerical worker in the insurance branch of the MDAS Corporation, one of the world’s leading supercompanies."
        n "Four years ago, you passed college with mediocre grades and a mountain of debt, but fortunately managed to secure this job. "
        n "Since then, things have not been easy, but then again, nothing in life is supposed to be easy. "
        n "Your parents raised a hard worker… most of the time. "
        n "It’s currently Wednesday morning. You sit in a seemingly endless room lined wall-to-wall with near-identical gray cubicles. "
        n "You answer emails, take calls from disgruntled customers, and write reports."
    
        n "One call, an exhausted-sounding woman sounds like she’s trying to hold back tears."
        Phone "“What do you mean it’s denied? I was supposed to be able to…”"
        n "You cut her off with a response from your checklist. "
        n "“We’re terribly sorry, ma’am, there’s nothing that can be done. Perhaps a different package will better suit your needs.”"
        Phone "“I don’t have the money for a different insurance package. The contract said-”"
        n "“We’re sorry, but the contract explicitly stated that the terms were subject to change. It’s unfortunate that you-” "
        Phone "“I can’t do this anymore…”"
        n "The woman begins to sob."

        phone "“I can’t do this anymore…” The woman begins to sob."

        menu:
            "Give her a refund.":
                $ refund = True

            "Follow the system.":
                $ system = True

        if refund:
        #put text for refund True
            n "You sigh, then check behind you. No sign of the floor manager roaming between the cubicles."
            n "“Listen, I can offer a partial refund. I’m really sorry, 50% is the best I can do.”"
            n "The woman’s voice is still close to crying, but you can tell that she will settle for this."
            Phone "“Thank you… thank you so-”"
            n "You hear a distant sound of metal dragging across metal and snap back into your corporate voice. "
            n "“No problem, Ma’am. Now if you could just give me your ID number so I can handle that…”"
            n "You finish up her call without issue."

        if system:
            #put text for if system is true
            n "You clench your jaw. This is the worst part of the job, always is. But it has to be done."
            n "“I’m…. terribly sorry. Perhaps I can redirect you to someone who-”"
            n "The woman hangs up. You sigh deeply."

        #continue text here
        n "The next few hours are more manageable. "
        n "People get angry with you and there’s always more emails to check and forms to stamp or sign, but that’s normal."
        n "Lunch break finally comes. You sigh with relief before standing and walking with the horde of co-workers to the lunchroom."
        n "You’re standing in one of the dozens of lines in front of the company-owned vending machines when Craig, your co-worker, approaches you. "
        n "Technically, Craig is your superior, but he’s always been nice to you."
        Craig "“Hey, [Name]! Listen, I was talking to some of the guys about Frank earlier."
        Craig "We thought it would be good if everyone donated a dollar or two to a fund to buy something for Frank’s widow."
        Craig "You know, something from all of us to help her out.”"
        n "Frank had collapsed in his cubicle with a heart attack last week."
        n "He had worked here much longer than you, but he was around 8 cubicles away, so you didn’t know him too well."
        n "You heard that the people in the cubicles next to them had heard him groaning a few hours before lunch, but nobody got up to check on him until the break started."
        n "You wonder if you had a heart attack, would your co-workers check on you?"
        n "How long did Frank struggle for breath while nobody came to help?"
        n "Craig’s voice pulls you back to reality."
        Craig "“[Name]? You good?”"
        n "“Oh! Yeah, sorry. Sure, I can give a dollar.”"
        n "Craig smiles as he puts the dollar into the shoebox."
        Craig "“Thanks, [Name]. Hey, are we still on for Friday?”"
        n "“Oh yeah, of course.”"
        n "You, Craig, and a bunch of the other clerical workers are planning on going out drinking on Friday, two days from now. "
        n "After all, morale is usually pretty low and prices drop the day after the Harvest."
        n "Oh, right."
        n "Tomorrow is the Day of the Harvest."
        n "You try not to think about it as you eat your protein bar, dry salad, and cookies."
        n "Soon enough, you return to work."
        n "…"
        n "After about another hour of work, you begin to hear the sound of metal dragging on metal in the distance."
        n "Please don’t stop here."
        n "You cringe as you hear the metallic screeching get louder, but under it you hear the sound of sleek shoes tapping on the ground."
        n "All around you, the normal muffled sounds of your co-workers on calls fall silent."
        n "The Floor Manager is here."
        e "“Zhang.”"
        n "You swivel your chair around and try your best to smile."
        n "“H-hello, Sir!”"
        n "The Floor Manager speaks to you in a voice that could never issue from a human mouth. "
I       n "It’s a sound that’s one part the rasp of a file on bone, one part grinding metal, and one part a distant scream –"
        n " - all somehow forming coherent words in your mind."

        if refund:
            #put text for refund True
            e "“You gave a partial refund at 10:32 to a customer who was not entitled to one. Exxxxxplain, meat.”"
            n "The Floor Manager is an Executive. Something you could never possibly hope to be."
            n "Far beyond human, having ripped the last weaknesses from his body. He’s a being of perfection now, intricate in his design and complete in every haunting detail."
            e "“Whelp. You have ten seconds to answer my query.”"
            n "The Floor Manager’s fingers are long curved hooks, tipped with barbs like fishhooks."
            n "They begin to twitch and rattle, like the Floor Manager is moments from ripping you apart."
            n "“S-sir, I felt that….”"
            n "The Floor Manager’s bloodshot eyes jitter as the chain-like loops of his head wind through each other, but his cloudy pupils stay focused on you."
            n "You look away, forcing yourself to stare at his luxurious suit."
            n "Of course, the Executives worked hard to earn this form. Only the most savvy and brilliant are allowed to transcend human limitations."
            n "Unlike you, the Floor Manager would never need to sleep or eat. His enhanced body and mind made him a true leader."
            n "You know that he can see time not as a set line, but as a branching set of paths that he can examine and choose from."
            n "An Executive never makes mistakes, never hesitates in their choices."
            n "They sacrificed everything for that power: their families, their morals, their humanity."
            n "You shudder and jolt back to reality. Hopefully, you didn’t pause long enough to anger him."
            n "“W-w-well, I felt that the client’s emotional state h-had reached a breaking point."
            n "A-and if I didn’t do something, then we would have l-lo-lost her future purchases?”"
            n "The suit is extravagant. It probably costs half a year’s worth of your rent to buy it, maybe more."
            n "You would never have a suit like that. You could barely afford your dress shirts, let alone something that beautiful."
            n "The Manager’s hooked claws rest on your shoulder, opening tiny cuts in your shirt with the slight touch. "
            n "You close your eyes and try not to let the Floor Manager see how hard you were shaking."
            e "“Accccceptable.”"
            n "He lifts his fingers off of you, opening a slit in the fabric, but leaving your skin intact."
            e "“But be warned, wretch- another mistake like that, and you will wish you were never born. Follow the protocol. No exxxxxceptions.”"
            n "The Floor manager dusts off his suit, his impossibly sharp digits somehow doing no damage to the fabric at all."
            e "“Ensure that thisssss…. Compassion of yours does not become an issue tomorrow.”"


        if system:
            #put text for if system is true
            e "“You’ve been performing… adequately, sssslug.”"
            n "The Floor Manager is an Executive. Something you could never possibly hope to be. "
            n "Far beyond human, having ripped the last weaknesses from his body."
            n "He’s a being of perfection now, intricate in his design and complete in every haunting detail."
            n "Of course, the Executives worked hard to earn this form. Only the most savvy and brilliant are allowed to transcend human limitations."
            n "Unlike you, the Floor Manager would never need to sleep or eat. His enhanced body and mind made him a true leader."
            n "You know that he can see time not as a set line, but as a branching set of paths that he can examine and choose from."
            n "An Executive never makes mistakes, never hesitates in their choices."
            n "But it comes at such a cost."
            n "You shudder and jolt back to reality. Hopefully, you didn’t pause long enough to anger him."
            n "“Th-thank you, Sir!”"
            n "The Floor Manager’s fingers are long curved hooks, tipped with barbs like fishhooks. They begin to twitch and rattle idly, a repetitive mechanical motion."
            e "“Perhaps by the end of the quarter, a sssssmall raise could be in order. Provided, of course, you do well tomorrow.”"
            n "The Floor Manager’s bloodshot eyes jitter as the chain-like loops of his head wind through each other, but his cloudy pupils stay focused on you."
            n "You look away, forcing yourself to stare at his luxurious suit."
            n "“Of course, Sir, tomorrow.”"
            n "His suit is extravagant. It probably costs half a year’s worth of your rent to buy it, maybe more."
            n "You would never have a suit like that. You can barely afford your dress shirts, let alone something that beautiful."
            e "“It is good that you understand the ssssignificanccce of tomorrow, meatbag. Be at the pickup location at 0900 hours.”"
            n "“O-of course, Sir. Absolutely.”"


        #continue text here
        n "The Floor Manager’s head turns all the way around, followed by his body, and then his legs each spin away as he stalks, humming, down the hall of cubicles."
        n "You struggle to catch your breath."
        n "You had signed up to help with the Harvest tomorrow as a last resort."
        n "Rent was going up, and even though you were scheduled for a 20 cent per hour raise by the end of the quarter, you needed a little extra cash to make it until then."
        n "The rest of the work day is uneventful."
        scene bg streets
        with fade
        n "…"
        n "The walk from the MDAS Company’s office to the subway station is short, but even so, you see a number of grimy homeless people as you walk."
        Waste "“Hey, [man/miss], can you spare some change?”"
        n "You avoid making eye contact. If they don’t have money today, it’s already far too late for them. Charity handouts won’t help them."
        Waste "“Anything helps. I just want to be off the streets tomorrow, you know?”"
        n "One is following you. You speed up, trying to avoid letting him touch you."
        Waste "“Come on, I don’t want to be out here when-”"
        n "You push through the turnstile at the subway entrance and walk quickly and silently to your stop."
        n "The ride home is silent, but you can’t shake away the thought of the people who you know won’t have enough for tomorrow."
        n "The company would say that they made their mistakes. It’s too late now."
        n "You just hope that’s true."
        scene bg room
        with fade
        n "…"
        n "You get home, kick off your shoes, drop your bag and collapse onto your couch."
        n "Your apartment is small and unimpressive, but it’s yours. Brown carpet, off-white walls."
        n "Cramped in some rooms and with some drafty windows, but it’s close to the subway and in a safe area."
        Skittles "“Mrow!”"
        n "Your cat, Skittles, scampers up to you."
        n "“Hey, girl! Sorry, work went rough tonight.”"
        Skittles "(purring)"
        n "“Oh, you want fresh food, huh?”"
        Skittles "“Mrow!”"
        n "You pour her a fresh bowl of food before heating up a bowl of instant ramen."
        n "You sit at your counter and watch a few videos on your phone, petting Skittles as she lays in your lap."
        n "You go to bed at a reasonable time, but don’t sleep well at all."
        n "You know what’s coming tomorrow."
        scene bg streets
        with fade
        n "…"
        n "The next morning, you shower, put on a dress shirt and pants, and give Skittles a few scratches before walking to the designated spot on your street."
        n "A smooth black van rolls to a stop in front of you before its door slides open. The inside is mostly empty, but a few people sit in seats along the side."
        n "They are dressed in black masks that cover their mouths and nose, sunglasses, disposable gloves, and long kitchen aprons."
        n "Their sleeves are rolled up. As you climb in, one hands you your uniform."
        n "You put it on wordlessly. Aside from the rumbling of the van as it accelerates, all is silent."
        n "The Harvest has begun."
        n "Most of the sacrifices are already accounted for. It’s a weeks-long process to round them up from the surrounding area and transport them to the city."
        n "But even so, part of the job is making sure that any undesirables on the streets are taken care of."
        n "It’s all for the bonus, you think to yourself. Somebody has to do it."
        n "It’s starting to get bright outside despite the endless haze of smog that always covers the sky."
        n "Driver “On the left. One sacrifice.”"
        n "You look out and see the same homeless man from last night limping down the empty street, glancing at the van in fear."
        n "What the hell is he doing outside today? He should have-"
        n "No. You can’t get emotional about this. It’s just the same as anyone else."
        n "The driver gestures to you."
        Driver "“Grab him.”"
        n "You are handed a syringe and rope."
        n "You grit your teeth behind your mask and climb out of the van as the homeless man runs down an alleyway."
        n "You chase after him. Even though you don’t exactly have time to exercise, he’s clearly in no state to run. You gain on him quickly."
        scene bg darkalley
        with fade
        Waste "“Please, [Man/Miss], I’m sorry! I can pay by the end of the week, I swear!”"
        n "You get closer. You aren’t sure what he’s talking about – really, it could be any number of debts. It doesn’t matter now."
        Waste "“Listen, I—”"
        n "You tackle him to the ground, and he begins sobbing."
        n "Can you really do this?"

        menu:
            "You can't":
                $ cannot = True

            "You have to":
                $ haveTo = True

        if cannot:
            n "You grit your teeth, then climb off him. It takes a few moments before he stops quivering and looks up at you."
            n "“Hide. Just stay out of sight for the rest of the day. I’ll say you escaped.”"
            Waste  "“Thank you! Thank you so much!”"
            n "You gesture for him to hide and walk back to the van."
            Driver "“Where is the sacrifice?”"
            n "“He escaped. Couldn’t find him. Maybe he hid in a building.”"
            Driver "“Forget it, we have a schedule to keep. Let’s move.”"

        if haveTo:
            n "You plunge the syringe into his grimy neck and press the plunger."
            n "“I’m sorry.”"
            n "He goes limp instantly. You tie his hands and call over someone else to help you drag him back to the van, where you lie him flat on the bed of the vehicle."
            scene bg streets
            with fade
        #text continues here
        n "No more words are exchanged as you continue to the pickup location."
        n "Eventually, you reach a featureless warehouse and help armed security staff in black riot gear force a crowd of bound and dirty people into the van. "
        n "Most are crying. There’s all ages – an old man here, a mother and a filthy child there. You try desperately not to look at them until the van doors are slammed shut."
        n "As you approach the Harvest site, the sound of a distant rhythm becomes audible. It’s timed like the beat of a heart, but sounds like the deep rumble of thunder."
        n "You are told to put in your earplugs shortly before the van rolls to a stop."
        n "Outside is a giant clearing in the endless skyscrapers. At its center is a huge, circular pit."
        n "The pit is larger than your apartment building’s footprint, and all around it are dozens of identical black vans and lines of people leading up to the edge."
        n "An enormous tower of thick and acrid black and red smoke floods out of the pit in time with the thundering pulse."
        n "The eerie red light from the pit paints strange shadows on the skyscrapers. "
        n "Despite still being early morning, the smoke blots out the sky, leaving everything in darkness. The windows of the skyscrapers are cast in an eerie blood-red glow."
        n "You grab a sacrifice out of the van and direct them to join the nearest line."
        n "They cringe at the deafening sound echoing from the pit and try to say something, but you cannot hear them."
        n "You unload your van’s load of people into a line and force them to march towards the pit. "
        n "You do your best not to look, but you know that you are being circulated towards the end as well. You have to take a turn Harvesting as part of the job, after all."
        n "The sound is getting louder and faster. Like a heart in the throes of excitement. Even with the earplugs, you can hear inhuman wailing and a roar like an engine."

        if cannot:
            n "You glance across the lines and see the homeless man you spared on your way to the pit."
            n "Your mouth goes dry."
            n "There was no chance for him after all."

        if haveTo:
            n "The man you captured groggily shuffles past you, barely conscious as the tranquilizer wears off. You do your best not to look at him."
            n "If not you, someone would have done it."
            n "If not this year, then next year."

        #back to normal text
        n "Inevitably, you find yourself at the edge of the pit."
        n "Below is a dizzying fall, hundreds of feet, so far you can only barely see the bottom through the haze of the bloody smoke."
        n "The enormous pit’s walls are all stained red, the shade growing deeper and darker as it descends."
        n "At the bottom, a vast engine roars."
        n "It is incomprehensibly huge, built like a twisted and inhuman heart made of metal and bone, with thousands of slurping tubes and thudding pistons and whirling gears."
        n "You feel dizzy looking at it, its enormous structure expanding and contracting in a way that nothing that huge should as acrid smog belches out of the smokestacks that cover it."
        n "It is the source of the world’s prosperity."
        n "The Engine of Industry."
        n "The Harvest is all for this - a ritual to fuel the vast machine of society itself."
        n "The cost is terrible, but prices must be paid. A machine cannot run without energy, and the world would fall apart if the Engine stopped."
        n "If the Engine stopped, you’d lose your job."
        n "If the Engine stopped, you would lose your home."
        n "If the Engine stopped, everything would be over."
        n "The apron-wearing woman at the front of the line taps your shoulder and gestures to you."
        n "You know what needs to be done."
        n "You clench your teeth and grip your knife."
        n "The first man is incredibly skinny, his skin covered in open sores."
        n "You glide the blade through his throat, letting his blood spill onto the edge of the pit."
        n "It joins the indistinguishable tide of blood coating the walls of the pit from hundreds already Harvested."
        n "You wait a while for her to drain before gesturing for the other person at the front to drag the body off for disposal."
        n "The next woman is nowhere near as dirty as the others. Perhaps she wasn’t homeless, but rent was due and she couldn’t pay."
        n "It doesn’t matter why you’re low on money when the Harvest begins, it only matters that anyone dragging down the economy must be dealt with."
        n "The Engine must have fuel. Without it, we would have nothing."
        n "Another, a teenager. You were still in high school at their age. How did this happen to them?"
        n "You slit their throat and your eyes go unfocused to the screaming and thudding of the Engine."
        n "Without the Harvest, we would starve, or be destitute."
        n "It ensures that the productive members of society are able to thrive and the worthless are purged."
        n "It pumps blood like a heart to all the megacorporations and businesses of the world to ensure that they succeed and keep society functioning."
        n "That’s what you were always told, and what you always believed."
        n "It’s little comfort now."
        n "Within about an hour, you stumble to the back of the line as your shift ends."
        n "Another masked and aproned figure loads you into a van. You strip off the gloves, the mask, the sunglasses, and the gory apron."
        n "Despite the precautions, your clothes are stained red. Your ears ring long after you are miles from the pit."
        n "You only now realize that you’ve been crying for the last hour."
        n "When you are dropped off at your apartment, you stagger to the elevator."
        n "You lurch into your apartment, where Skittles greets you, unaware of what you did today."
        n "You collapse to the couch and hold her. She’s so small and delicate."
        n "She purrs softly."
        n "You receive a text notification from the MDAS Corporation."
        Phone "“Thank you for your participation in this year’s Harvest! Your bonus has already been deposited in your account.”"
        Phone "“Feel free to enjoy the rest of your day off – you’ve earned it!”"
        Phone "“But remember, your job resumes tomorrow. See you at 9:00!”"
        Phone "“Sincerely, the MDAS Corporation”"
        n "You let your phone fall to the ground and begin to sob."


        jump the_end








    label sacrafice_block_path:
        e "The line is red. Going down. You try to control your breathing. The only thing worse than bad numbers is being caught lying. Bad, sir."
        e "The exec screeches, a sound like knives being dragged across metal. Your ears are still ringing as he grips your shoulders and drags you away from your cubicle."
        e "Not good, not good, whelp! We need those numbers back up! You are reassigned. It's an important day."

        e "The boss loads you to a van with blacked out windows. You climb You are told to remove your suit and tie - you don't want them getting stained more than they already are. You put on some sunglasses - official uniform."
        e "You put in your earplugs - once the Harvest begins in earnest, the engine will deafen you without protection. Finally, you put on a pair of disposable gloves - official policy." 
        e "You step out into the haze at the pit. The Harvest is about to begin. At least you didn't have to round them up."

        e "You march to the edge of the pit. A woman dressed like you marches a dirty man over to you. He's covered in holes from body mods - remnants of jobs that didn't pan out."
        e "You absently rub the port at the base of your skull - then remember why you are here. A buzz rings over the sound of the engine of progress's thudding heartbeat - the signal to begin."
        e "You stare at the knife in your hand, then down at the filthy waste of space whose head is now sitting over the edge of the pit. You kneel down and put the blade to his throat."

        e "The market is thirsty"
        
        e "Begin the harvest."

        e "You swipe the knife across the man's throat like a card through a reader. Just a swipe, purposeful and smooth. He deserves that much, at least. He gurgles as he chokes on his last breath as it bubbles past the flow of blood."
        e "You keep your knee on his back, but he doesn't struggle. A minute passes before he's empty. A co-worker you can't remember the name of comes over to collect the drained body and drag it to the furnace chute. The engine grows louder. At least this will improve the numbers."

        e "Another victim is pushed down to the chopping block. This one is crying, she is begging for a chance to pay her rent, she has the money, she swears. She takes another minute to drain."
        e "Just let it happen, there's no point in fighting this. If nobody is sacrificed, the economy would suffer. If the economy suffers, everyone suffers. "
        e "If a few have to have an unpleasant death for you and everyone you know to go to bed with a full belly and a roof over your head, then so be it."
        e "You are sorry for the first few. But they blur together."
        e "By the end of the Harvest, your eyes are glazed over and your hands shake. The gloves are filled with sweat."
        e "The engine screams its approval and belches its delight into the sky with clouds of red and black."
        e "You stumble back to the van. You get the rest of the day off."

        jump the_end


    label chopping_block_path:
        e "The line goes up. Green. You cough out Good! they are good. P-profit! The boss's many needle teeth clink in his vast mouth. From the upper jaw all the way down to the collar of his suit is a series of fused needles and metal thorns that tap together one after another."
        e "Tip-tap, over and over. Click-clack, so much noise. 
        Glad to hear it, worm. Keep working."
        e "He slaps your back, tearing your cheap garbage suit and ripping into your soft human skin. You whimper, but don't say anything." 
        e "This suit isn't worth it. Besides, complaining about pain to an exec means nothing now that they have escaped the feeble state of humanity."
        e "The exec buzzes and clicks. You hear the tap of crisp shoes on the ground as he walks away, but you know that he is still watching you with one of his eyes. Even once he leaves your cubicle, he is watching you. Always."

        e "A few hours of feverish work pass before the intercom buzzes over the clacking of dozens of keyboards. 
        ATTENTION LOYAL WORKERS. THE DAY OF THE HARVEST IS HERE. TURN YOUR ATTENTION TO YOUR SCREENS FOR THIS IMPORTANT MOMENT."
        e "Your eyes unfocus as the wall of numbers is replaced by a grainy view of a massive pit. You've seen this so many times, can't you just skip it? You have a lot of work to do and this is the same every time."
        e "The pit grows darker and darker as it gets deeper, stained by generations of blood pooling and drying. Rings of filthy people are lined up around the edge of the pit, their heads over the lip."
        e "Behind each sacrifice, a man or woman in a simple collared shirt."


        e "The Harvest finally begins"

        e "Each sacrifice's throat is carved open and allowed to drain into the gaping maw. At its center beats the heart of the market, the engine of industry greedily lapping up its offering."
        e" The empty bodies are tossed into a chute added to its furnace. The machine roars louder and louder, eventually rendering the audio of the broadcast silent to prevent damage to the speakers."
        e "The display continues for minutes. Maybe hours. It's much less nauseating after so many harvests. It's hard to watch, but without a little grease for the gears, how can the market thrive?"
        e " Finally, the broadcast ends. The numbers are definitely good now. Nothing like a little bit of blood to really breathe some life into the economy. You keep working. There's a lot more to do today."

        jump the_end


    label business_story:
        e " The CEO stands over you, his head a rotating steel cage of fused needles in the shape of a dodecahedron."
        e" At its center is a single massive, bloodshot eye that twitches back and forth in a blur of rotation, but never lets its foggy pupil off of you. 
        He is so very beautiful."
        e "His hooked fingers reach over to you, whirring as they writhe through the air before suddenly becoming still as they find your suit. "
        e" The CEO has long since forsaken the need for a mouth, and speaks directly into your mind as the raised veins on his massive eye throb and expand.
        Your harvest this year was more than satisfactory. The great transaction continues."

        
        e "You know, Anders, you might have what it takes to be an exec after all. What do you say?" (Boss)

        
        menu:
                "I'd be honored":

                    jump honored_path
                
                "You feel regret creep into your heart":

                    jump regret_path

    label honored_path:
    #Need to adjust this for when the CEO speaks to switch to them being the one speaking.
    e "The CEO must be pleased, for he strokes your face with the back of his massive skeletal hand, not letting his blades sink into your soft human flesh. You know, Anders, you might have what it takes to be an exec after all. What do you say? "

    e "All your dicipline has paid off. All your hours of grind, all your sacrifices."
    
    e "The saws come towards your soft flesh and you do not flinch as they open you up. The pain is excrutiating, but you have come much too far to let that stop you. "
    
    e "Piece by piece, they peel off the parts of yourself that you don't need. You are a perfect engine of profit, a being with none of the weaknesses you once had. Last is your heart."
    
    e "You weren't using it much anyway. Your bonus is going to be huge this quarter. No more sleep. No more need for dreams when your dream has finally been realized, after all."

    e "Your new body is so sharp. The world is so bright, moves so slowly. So much noise, so many angles you can view. Behind the veil of this world is an endless series of transactions, a perfect system where energy all moves towards those who truly deserve it."
    
    e "You are so very beautiful now. The numbers are good."

    e "You recieved the promotion you were working for after all. So many bodies, and you should be proud! But even though you are an exec, you aren't a CEO yet - there's still worlds of profit to be made."

    jump the_end


    label regret_path: 

    e "You think of the screams."
    e "So many people harvested this year."
    e "Of course, the surplus population must be dealt with somehow. If they aren't willing to work, why bother living?"
    e "You think of the youngest one in that crowd, a thin boy with ripped sweatpants. Couldn't have been much more than 15. Must have been a dropout."
    e "You think of his blood gushing from the jagged slash in his throat, of the pool of gore at the bottom of the pit as your underlings held the sacrifices down and drained them."
    e "The sound of rumbling deep in the pit."
    e "A great machine roared to life, refueled."
    e "The sky blackens as the great engine of industry began to howl again, its vents greedily slurping the sacrificial blood as the dried husks are tossed into its waiting furnace."
    e "But you let doubt into your mind."
    e "You return to reality."
    e "The CEO's eye is focused on you."
    menu:
            "Apologize":

                jump death_path
            
            "Accept your fate":

                jump almost_path

    label death_path:
    
    e "The CEO does not hesitate. You don't even have time to react before your head is in multiple pieces, your brain matter splattered across the marble floor."
    e "A janitor is already rushing in before your body is cold. Fortunately, not a single drop of gore got on your suit - the CEO recognizes value when he sees it."
    e "Unfortunately, you proved you didn't have what it takes."

    jump the_end



    label almost_path:

    e "The eye rolls away and focuses outside the window, letting the spindly body of the CEO follow shortly after in a lazy pirouette. His enormous arms cross behind him, twitching and writhing at the tips of his fingers.  "

    e "That's what I like about you, Anders. You might be a low-rent waste of space, but you know never to apologize."

    e "His voice is a hoarse whisper, a choke from a strangled throat."
    
    e " Maybe if you put in some real elbow grease, you might still be an exec."
    e " You nod, barely believing that such a show of weakness went unpunished."
    e "Leave. I'll see you in the boardroom. tomorrow. His eye whirls back to fix you with a final, baleful stare."
    e "And everywhere else."

    e "Close, but not quite! You must purge your mind of weakness and embrace the grind if you wish to truly succeed!"

    jump the_end



    label ceo_path:

    e "Your time was first.
    Your family was second.
    Your body was third.
    Your life was last."

    e "But now you are perfect"
    e "Look directly into the market and see its pulse beat wildly as the world chokes on its blood and the heart of profit gets faster and faster."
    e "Your body is gone and you never needed it because you were never truly there. You are a husk puppetted by desire and greed and you are perfect now."
    e "Your many eyes spin wildly in the cage of metal you built for them. No lids to close, no time wasted on sleep. You are beyond what you once thought possible. No hunger, no need for anything at all."


    e "You are an executive now, a perfected engine of masterful beauty. Women fall before you in horror and awe as the worthless rabble scream in adoration. You abandoned them long ago, their cries of fear and exultation mean nothing to a perfect being."
    e "You are beyond them."
    e "You are exquisite and perfect and finally pure."
    e" Reach up to the sky with your long sharp fingers and feel them slip beneath the skin of the world. Feel it tear as you pull it apart into a new form that pleases you. What is the world to you? Nothing, not even a home. It is a resource, a trophy, a source of entertainment. "
    e" Drink their blood, steal their air, watch them beg to join you from every direction as your spinning cage of eyes focuses on the horrified and blind faces of all the filthy people."

    e " They are nothing to you"

    e "You are everything"

    e " Congratulations! You have the CEO mindset! You know what matters and hive the drive to achieve it!
    ou must be proud!"  
    
    jump the_end

    


        # ... the game continues here
    label the_end:

    e " This is the end of the game."

    if persistent.gameDone:
    
        e "Alternate path may have been unlocked."
        
    $ persistent.gameDone = True

    # This ends the game. 

    return
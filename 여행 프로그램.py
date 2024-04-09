q = input("Would you like to input in English or Korean? ")
if q.lower() == "english":
    rec_menu = ["Busan", "Seoul", "Suwon", "Daejeon", "Jeju Island", "Gangneung", "Ulsan", "Gwangju"]
    place_list = [
        ["Haeundae Beach", "Beomeosa Temple"],  
        ["Gyeongbokgung Palace", "Namsan Seoul Tower"],  
        ["Hwaseong Palace", "Suwon Hwaseong Fortress"], 
        ["Hanbat Arboretum", "Daejeon Culture & Arts Center"],  
        ["Hallasan", "Seongsan Ilchulbong Peak"],  
        ["Gangneung Beach", "Ojukheon House"],  
        ["Ulsan Grand Park", "Daewangam Park"],  
        ["Gwangju Lake", "Hill of the Magic"],
    ]
    travel_list = []
    while True:
        print("-" * 50)
        print("        Travel Place Management Program       ")
        print("-" * 50)
        print("1. Print List of Travel Places")
        print("2. Add a Travel Place")
        print("3. Delete a Travel Place")
        print("4. Get a Recommendation for Travel Place")
        print("5. Exit")
        menu = int(input("Please enter the menu: "))
        if menu == 1:
            if not travel_list:
                print("There are no travel places in the list.")
            else:
                print("List of Travel Places:", *travel_list)
        elif menu == 2:
            place = input("Which travel place do you want to add?: ")
            flag = False
            for i in travel_list:
                if i == place:
                    flag = True
            if flag:
                print(f"The travel place {place} is already in the list.")
            else:
                travel_list.append(place)
                print(f"{place} has been added to the travel places.")
        elif menu == 3:
            if not travel_list:
                print("There are no travel places in the list.")
            else:
                print("List of travel places to delete:", *travel_list)
                place = input("Which travel place do you want to delete?: ")
                if place in travel_list:
                    travel_list.remove(place)
                    print(f"{place} has been deleted from the travel places.")
                else:
                    print("The specified travel place does not exist in the list.")
        elif menu == 4:
            for i, place in enumerate(rec_menu, start=1):
                print(f"{i}) {place}", end=" ")
            print()
            choice = int(input("Which location would you like to receive a recommendation for?: "))
            if 1 <= choice <= len(rec_menu):
                print(f"In {rec_menu[choice - 1]}, there are places such as {', '.join(place_list[choice - 1])}.")
                p = input("Would you like to add this location? (yes or no): ")
                if p.lower() == "yes":
                    flag = False
                    for i in travel_list:
                        if i == rec_menu[choice - 1]:
                            flag = True
                    if flag:
                        print(f"The travel place {rec_menu[choice - 1]} is already in the list.")
                    else:
                        travel_list.append(rec_menu[choice - 1])
                        print(f"{rec_menu[choice - 1]} has been added to the list of travel places.")
                else:
                    print("Adding canceled.")
            else:
                print("Please enter again.")
        elif menu == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid menu number. Please try again.")
elif q.lower() == "korean":
    rec_menu = ["부산", "서울", "수원", "대전", "제주도", "강릉", "울산", "광주"]
    place_list = [
        ["해운대 해수욕장", "범어사"],  
        ["경복궁", "남산서울타워"],    
        ["화성행궁", "수원화성"],       
        ["한밭수목원", "대전예술의전당"], 
        ["한라산", "성산일출봉"],       
        ["강릉해변", "오죽헌"],        
        ["울산대공원", "대왕암공원"],    
        ["광주호", "마술의 언덕"]       
    ]
    travel_list = []
    while True:
        print("-" * 50)
        print("          여행 장소 관리 프로그램        ")
        print("-" * 50)
        print("1. 여행장소 목록 출력")
        print("2. 여행장소 추가")
        print("3. 여행장소 삭제")
        print("4. 여행장소 추천")
        print("5. 종료하기")
        menu = int(input("메뉴를 입력해주세요:"))
        if menu == 1:
            if not travel_list:
                print("리스트에 여행장소가 없습니다.")
            else:
                print("여행장소 목록:", *travel_list)
        elif menu == 2:
            place = input("어떤 여행지를 추가 할까요?: ")
            flag = False
            for i in travel_list:
                if i == place:
                    flag = True
            if flag:
                print(f"여행지 리스트에 {place}이(가) 있습니다.")
            else:
                travel_list.append(place)
                print(f"{place} 여행지가 추가되었습니다.")
        elif menu == 3:
            if not travel_list:
                print("리스트에 여행장소가 없습니다.")
            else:
                print("삭제할 여행지 목록:", *travel_list)
                place = input("어떤 여행지를 삭제할까요?: ")
                if place in travel_list:
                    travel_list.remove(place)
                    print(f"{place} 여행지가 삭제되었습니다.")
                else:
                    print("해당 여행지가 목록에 존재하지 않습니다.")
        elif menu == 4:
            for i, place in enumerate(rec_menu, start=1):
                print(f"{i}) {place}", end=" ")
            print()
            choice = int(input("몇 번째 지역을 추천 받으시겠습니까?: "))
            if 1 <= choice <= len(rec_menu):
                print(f"{rec_menu[choice - 1]}에는 {', '.join(place_list[choice - 1])}과 같은 곳이 있습니다.")
                p = input("이 지역을 추가하시겠습니까? (yes or no): ")
                if p.lower() == "yes":
                    flag=False
                    for j in travel_list:
                        if j==rec_menu[choice-1]:
                            flag=True
                    if flag==True:
                        print(f"여행지 리스트에 {rec_menu[choice-1]}이(가) 이미 있습니다.")
                    else:
                        travel_list.append(rec_menu[choice-1])
                        print(f"여행지 리스트에 {rec_menu[choice-1]}을 추가 했습니다.")
                else:
                    print("추가를 취소합니다.")
            else:
                print("다시 입력 해주세요") 

        elif menu == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효하지 않은 메뉴 번호입니다. 다시 입력해주세요.")
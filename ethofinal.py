import json

class country():
    data =json.load(open("Final.json","r",encoding="utf-8"))
          
    @staticmethod
    def country_list():
         """
        Get a list of all country names in the dataset.

        Returns:
        list: A list of country names.
        """
         a=[]
         for i in data.keys():
             a.append(i)
         return(a)

    def country_summary(country_name="India"):
         """
        Get a summary of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the summary. Default choice is "India".

        Returns:
        str: A summary of the specified country will be returned in a string format.

        Examples
        --------        
        >>> etho.country_summary()
        'India is a country in Asia that is home to 1,380,004,000 people. It is also home to 424 living indigenous languages. One of these, Hindi, is an official language of the country. Others—Assamese, Assamese, Bengali, Bengali, Eastern Punjabi, Eastern Punjabi, Garo, Garo, Gujarati, Gujarati, Kannada, Kannada, Kashmiri, Kashmiri, Khasi, Khasi, Konkani, Konkani, Maithili, Maithili, Malayalam, Malayalam, Marathi, Marathi, Meitei, Meitei, Nepali, Odia, Odia, Tamil, Telugu, Telugu, Urdu, and Urdu—are official languages in parts of the country. India was also home to 11 indigenous languages that are now extinct. In addition, 29 living non-indigenous languages are established within the country. One of these, English, is also an official language of the country. In formal education, 26 indigenous languages are used as languages of instruction.'  

        >>> etho.country_summary('China')
        'China is a country in Asia that is home to 1,412,600,000 people. It is also home to 281 living indigenous languages. One of these, Mandarin Chinese, is the official language of the country. Others—Central Tibetan, Kyrgyz, and Uyghur—are official languages in parts of the country. China was also home to 2 indigenous languages that are now extinct. In addition, 25 living non-indigenous languages are established within the country. In formal education, 7 indigenous languages are used as languages of instruction.'

        """
         return(data[country_name]['summary'])

    def country_officialname(country_name="India"):
         """
        Get the official name of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the official name. Default choice is "India".

        Returns:
        str: The official name of the specified country will be returned in a string format.

        Examples
        --------
        >>> etho.country_officialname()
        'Republic of India'

        >>> etho.country_officialname('Australia')
        'Commonwealth of Australia
        
        """
         return(data[country_name]['official_name'])

    def country_code(country_name="IN"):
         """
        Get the country code (ISO3166) of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the country code. Default choice is "IN".

        Returns:
        str: The country code (ISO3166) of the specified country will be returned in a string format.
        """
         return(data[country_name]['country_code(ISO3166)'])

    def country_area(country_name="India"):
         """
        Get the area of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the area. Default choice is "India".

        Returns:
        str: The area of the specified country will be returned in string format as 'square kilometers'.
        """
         return(str(data[country_name]['area(sq_km)'])+" Square Kilometer")

    def country_commencement(country_name="India"):
         """
        Get the commencement year of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the commencement year. Default choice is "India".

        Returns:
        int: The commencement year of the specified country will be returned in integer format.
        """
         return(data[country_name]['commencement'])

    def country_continent(country_name="India"):
         """
        Get the continent of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the continent. Default choice is "India".

        Returns:
        str: The continent of the specified country will be returned in a string format.
        """
         return(data[country_name]['continent'])

    def country_families(country_name="India"):
         """
        Get the language families present in the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the language families. Default choice is "India".

        Returns:
        str: The language families present in the specified country will be returned in a string format.
        """
         return(data[country_name]['families'])

    def country_vitality(country_name="India"):
         """
        Get the vitality of languages in the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the language vitality. Default choice is "India".

        Returns:
        list: The vitality of languages in the specified country will be returned as a list format.
        """
         return(data[country_name]['vitality'])

    def continent_countries(continent="Asia"):
         """
        Get a list of countries in the specified continent.

        Parameters:
        continent_name : str, optional
            The name of the continent will be given to retrieve the list of countries. Default choice is "Asia".

        Returns:
        list: A list of country names in the specified continent will be returned in list format.
        """
         conti=[]
         for i in data.keys():
             if(data[i]['continent'] == continent):
                 conti.append(i)
         return(conti)

    def total_countries():
         """
        Print the total number of countries in the dataset.
        """
         print(len(_data.keys()))

    def continent_length(continent="Asia"):
         """
        Get the total number of countries in the specified continent.

        Parameters:
        continent_name : str, optional
            The name of the continent will be given to retrieve the number of countries. Default choice is "Asia".

        Returns:
        int: The total number of countries in the specified continent will be returned in integer format.
        """
         conti=[]
         for i in _data.keys():
             if(_data[i]['continent'] == continent):
                 conti.append(i)
         return(len(conti))

    def country_languages(country_name="India"):
        """
        Get a list of languages spoken in the specified country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrieve the list of languages.

        Returns:
        list: A list of languages spoken in the specified country will be returned in a list format.
        """
        x = []
        for i in _data[country_name]['languages']:
            x.append(i)
        return x

class languages(country):
    @staticmethod   
    def language_summary( country_name="India", lang="Tamil"):
        """
        Get the summary of the specified language spoken in the country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrive the specified country's language.
        
        lang : str, mandatory
            The name of the language will be given to retrieve the specified language's summary.

        Returns:
        str: A summary of the specified language spoken in the country will be returned in a string format.
        """
        return (_data[country_name]['languages'][lang]['summary'])

    def language_code(country_name="India", lang="Tamil"):
        """
        Get the language code (ISO639) of the specified language spoken in the country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrive the specified country's language.

        lang : str, mandatory
            The name of the language will be given to retrieve the specified language's code.

        Returns:
        str: The language code (ISO639) of the specified language spoken in the country will be returned in a string format.
        """
        return (_data[country_name]['languages'][lang]['language_code(ISO639)'])

    def language_population(country_name="India", lang="Tamil"):
        """
        Get the population estimate of speakers for the specified language in the country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrive the specified country's language.

        lang : str, mandatory
            The name of the language will be given to retrieve the specified language's population.

        Returns:
        str: The population estimate of speakers for the specified language in the country will be returned in a string format.
        """
        return (_data[country_name]['languages'][lang]['population'])

    def language_family(country_name="India", lang="Tamil"):
        """
        Get the language family to which the specified language belongs in the country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrive the specified country's language.

        lang : str, mandatory
            The name of the language will be given to retrieve the specified language's family.

        Returns:
        str: The language family to which the specified language belongs in the country will be returned in a string format.
        """
        return (_data[country_name]['languages'][lang]['family'])

    def lang_to_country(lang="Tamil"):

     """Returns all the properties of country based on the language"""

     for i in _data.keys():
            a=[]
            for j in _data[i]['languages'].keys():
                a.append(j)
            for k in a:
                l=str(lang).capitalize()
                if(l == k):
                    print(i)
                    break
    def name(code):
        for i in _data.keys():
            for j in _data[i]["languages"]:
                a=[]
                a.append(_data[i]["languages"][j]["language_code(ISO639)"])
                for k in  a:
                    if (code == k):
                        print(i)

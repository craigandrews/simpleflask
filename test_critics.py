import pytest
import responses
from critics import URL, get_critics
import json

expected_result = {
    "copyright":"Copyright (c) 2021 The New York Times Company. All Rights Reserved.",
    "num_results":82,
    "results":[
       {
          "bio":"A. O. Scott joined The New York Times as a film critic in January 2000, and was named a chief critic in 2004. Previously, Mr. Scott had been the lead Sunday book reviewer for Newsday and a frequent contributor to Slate, The New York Review of Books, and many other publications. \n<br/><br/>\nIn the 1990s he served on the editorial staffs of Lingua Franca and The New York Review of Books. He also edited \"A Bolt from the Blue and Other Essays,\" a collection by Mary McCarthy, which was published by The New York Review of Books in 2002. \n<br/><br/>\nMr. Scott was a finalist for the Pulitzer Prize in Criticism in 2010, the same year he served as co-host (with Michael Phillips of the Chicago Tribune) on the last season of \"At the Movies,\" the syndicated film-reviewing program started by Roger Ebert and Gene Siskel.\n<br/><br/>\nA frequent presence on radio and television, Mr. Scott is Distinguished Professor of Film Criticism at Wesleyan University and the author of Better Living Through Criticism, forthcoming in 2016 from The Penguin Press. A collection of his film writing will be published by Penguin in 2017. \n<br/><br/>\nHe lives in Brooklyn with his family.",
          "display_name":"A. O. Scott",
          "multimedia":{
             "resource":{
                "credit":"Earl Wilson/<br/>The New York Times",
                "height":163,
                "src":"http://static01.nyt.com/images/2015/10/07/topics/ao-scott/ao-scott-articleInline.jpg",
                "type":"image",
                "width":220
             }
          },
          "seo_name":"A-O-Scott",
          "sort_name":"A. O. Scott",
          "status":"full-time"
       },
       {
          "bio":"",
          "display_name":"Renata Adler",
          "multimedia":"null",
          "seo_name":"Renata-Adler",
          "sort_name":"Adler, Renata",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Robert Alden",
          "multimedia":"null",
          "seo_name":"Robert-Alden",
          "sort_name":"Alden, Robert",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Eugene Archer",
          "multimedia":"null",
          "seo_name":"Eugene-Archer",
          "sort_name":"Archer, Eugene",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Miriam Bale",
          "multimedia":"null",
          "seo_name":"Miriam-Bale",
          "sort_name":"Bale, Miriam",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Felicity Barringer",
          "multimedia":"null",
          "seo_name":"Felicity-Barringer",
          "sort_name":"Barringer, Felicity",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Richard Bernstein",
          "multimedia":"null",
          "seo_name":"Richard-Bernstein",
          "sort_name":"Bernstein, Richard",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Ben Brantley",
          "multimedia":"null",
          "seo_name":"Ben-Brantley",
          "sort_name":"Brantley, Ben",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"D. J. R. Bruckner",
          "multimedia":"null",
          "seo_name":"D-J-R-Bruckner",
          "sort_name":"Bruckner, D. J. R. ",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Paul Brunick",
          "multimedia":"null",
          "seo_name":"Paul-Brunick",
          "sort_name":"Brunick, Pual",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Tom Buckley",
          "multimedia":"null",
          "seo_name":"Tom-Buckley",
          "sort_name":"Buckley, Tom ",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Kevin Cahillane",
          "multimedia":"null",
          "seo_name":"Kevin-Cahillane",
          "sort_name":"Cahillane, Kevin",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Vincent Canby",
          "multimedia":"null",
          "seo_name":"Vincent-Canby",
          "sort_name":"Canby, Vincent",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Jeannette Catsoulis",
          "multimedia":"null",
          "seo_name":"Jeannette-Catsoulis",
          "sort_name":"Catsoulis, Jeannette",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Carina Chocano",
          "multimedia":"null",
          "seo_name":"Carina-Chocano",
          "sort_name":"Chocano, Carina",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"John Corry",
          "multimedia":"null",
          "seo_name":"John-Corry",
          "sort_name":"Corry, John",
          "status":""
       },
       {
          "bio":"",
          "display_name":"B. R. Crisler",
          "multimedia":"null",
          "seo_name":"B-R-Crisler",
          "sort_name":"Crisler, B. R.",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Bosley Crowther",
          "multimedia":"null",
          "seo_name":"Bosley-Crowther",
          "sort_name":"Crowther, Bosley",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Nina Darnton",
          "multimedia":"null",
          "seo_name":"Nina-Darnton",
          "sort_name":"Darnton, Nina",
          "status":""
       },
       {
          "bio":"",
          "display_name":"David DeWitt",
          "multimedia":"null",
          "seo_name":"David-DeWitt",
          "sort_name":"DeWitt, David",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Jennifer Dunning",
          "multimedia":"null",
          "seo_name":"Jennifer-Dunning",
          "sort_name":"Dunning, Jennifer",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Richard Eder",
          "multimedia":"null",
          "seo_name":"Richard-Eder",
          "sort_name":"Eder, Richard",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Anita Gates",
          "multimedia":"null",
          "seo_name":"Anita-Gates",
          "sort_name":"Gates, Anita",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Neil Genzlinger",
          "multimedia":"null",
          "seo_name":"Neil-Genzlinger",
          "sort_name":"Genzlinger, Neil",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Morris Gilbert",
          "multimedia":"null",
          "seo_name":"Morris-Gilbert",
          "sort_name":"Gilbert, Morris",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Harry Gilroy",
          "multimedia":"null",
          "seo_name":"Harry-Gilroy",
          "sort_name":"Gilroy, Harry",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Daniel M. Gold",
          "multimedia":"null",
          "seo_name":"Daniel-M-Gold",
          "sort_name":"Gold, Daniel M.",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Walter Goodman",
          "multimedia":"null",
          "seo_name":"Walter-Goodman",
          "sort_name":"Goodman, Walter",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Jack Gould",
          "multimedia":"null",
          "seo_name":"Jack-Gould",
          "sort_name":"Gould, Jack",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Roger Greenspun",
          "multimedia":"null",
          "seo_name":"Roger-Greenspun",
          "sort_name":"Greenspun, Roger",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Mike Hale",
          "multimedia":"null",
          "seo_name":"Mike-Hale",
          "sort_name":"Hale, Mike",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Mordaunt Hall",
          "multimedia":"null",
          "seo_name":"Mordaunt-Hall",
          "sort_name":"Hall, Mordaunt ",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Donal J. Henahan",
          "multimedia":"null",
          "seo_name":"Donal-J-Henahan",
          "sort_name":"Henahan, Donal J.",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Nicole Herrington",
          "multimedia":"null",
          "seo_name":"Nicole-Herrington",
          "sort_name":"Herrington, Nicole",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Caryn James",
          "multimedia":"null",
          "seo_name":"Caryn-James",
          "sort_name":"James, Caryn",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Stanley Kauffman",
          "multimedia":"null",
          "seo_name":"Stanley-Kauffman",
          "sort_name":"Kauffman, Stanley",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Dave Kehr",
          "multimedia":"null",
          "seo_name":"Dave-Kehr",
          "sort_name":"Kehr, Dave",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Ben Kenigsberg",
          "multimedia":"null",
          "seo_name":"Ben-Kenigsberg",
          "sort_name":"Kenigsberg, Ben",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Laura Kern",
          "multimedia":"null",
          "seo_name":"Laura-Kern",
          "sort_name":"Kern, Laura",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Peter Kihss",
          "multimedia":"null",
          "seo_name":"Peter-Kihss",
          "sort_name":"Kihss, Peter",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Wayne King",
          "multimedia":"null",
          "seo_name":"Wayne-King",
          "sort_name":"King, Wayne",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Anna Kisselgoff",
          "multimedia":"null",
          "seo_name":"Anna-Kisselgoff",
          "sort_name":"Kisselgoff, Anna",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Hilton Kramer",
          "multimedia":"null",
          "seo_name":"Hilton-Kramer",
          "sort_name":"Kramer, Hilton",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Nathan Lee",
          "multimedia":"null",
          "seo_name":"Nathan-Lee",
          "sort_name":"Lee, Nathan",
          "status":"part-time"
       },
       {
          "bio":"Manohla Dargis is the co-chief film critic for The Times, where she started in 2004. She has also written for The Los Angeles Times, where she was a chief film critic, and for the LA Weekly, where she was both a film critic and the film editor. She lives in Los Angeles.",
          "display_name":"Manohla Dargis",
          "multimedia":"null",
          "seo_name":"Manohla-Dargis",
          "sort_name":"Manohla Dargis",
          "status":"full-time"
       },
       {
          "bio":"",
          "display_name":"Ernest Marshall",
          "multimedia":"null",
          "seo_name":"Ernest-Marshall",
          "sort_name":"Marshall, Ernest",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Ned Martel",
          "multimedia":"null",
          "seo_name":"Ned-Martel",
          "sort_name":"Martel, Ned",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Janet Maslin",
          "multimedia":"null",
          "seo_name":"Janet-Maslin",
          "sort_name":"Maslin, Janet",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Herbert L. Matthews",
          "multimedia":"null",
          "seo_name":"Herbert-L-Matthews",
          "sort_name":"Matthews, Herbert L.",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Patricia S. McCormick",
          "multimedia":"null",
          "seo_name":"Patricia-S-McCormick",
          "sort_name":"McCormick, Patricia S.",
          "status":""
       },
       {
          "bio":"",
          "display_name":"John T. McManus",
          "multimedia":"null",
          "seo_name":"John-T-McManus",
          "sort_name":"McManus, John T.",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"W. L. Middleton",
          "multimedia":"null",
          "seo_name":"W-L-Middleton",
          "sort_name":"Middleton, W. L.",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Elvis Mitchell",
          "multimedia":"null",
          "seo_name":"Elvis-Mitchell",
          "sort_name":"Mitchell, Elvis",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Herbert Mitgang",
          "multimedia":"null",
          "seo_name":"Herbert-Mitgang",
          "sort_name":"Mitgang, Herbert",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Charles Morgan",
          "multimedia":"null",
          "seo_name":"Charles-Morgan",
          "sort_name":"Morgan, Charles",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Richard W. Nason",
          "multimedia":"null",
          "seo_name":"Richard-W-Nason",
          "sort_name":"Nason, Richard W.",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Victor Navasky",
          "multimedia":"null",
          "seo_name":"Victor-Navasky",
          "sort_name":"Navasky, Victor",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Peter M. Nichols",
          "multimedia":"null",
          "seo_name":"Peter-M-Nichols",
          "sort_name":"Nichols, Peter M.",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Holcomb B. Noble",
          "multimedia":"null",
          "seo_name":"Holcomb-B-Noble",
          "sort_name":"Noble, Holcomb B.",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Frank S. Nugent",
          "multimedia":"null",
          "seo_name":"Frank-S-Nugent",
          "sort_name":"Nugent, Frank S.",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Suzanne O'Connor",
          "multimedia":"null",
          "seo_name":"Suzanne-OConnor",
          "sort_name":"O'Connor, Suzanne",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Jon Pareles",
          "multimedia":"null",
          "seo_name":"Jon-Pareles",
          "sort_name":"Pareles, John",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Thomas M. Pryor",
          "multimedia":"null",
          "seo_name":"Thomas-M-Pryor",
          "sort_name":"Pryor, Thomas M.",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Nicolas Rapold",
          "multimedia":"null",
          "seo_name":"Nicolas-Rapold",
          "sort_name":"Rapold, Nicolas",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Julie Salamon",
          "multimedia":"null",
          "seo_name":"Julie-Salamon",
          "sort_name":"Salamon, Julie",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Rachel Saltz",
          "multimedia":"null",
          "seo_name":"Rachel-Saltz",
          "sort_name":"Saltz, Rachel",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Nora Sayre",
          "multimedia":"null",
          "seo_name":"Nora-Sayre",
          "sort_name":"Sayre, Nora",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Harold C. Schonberg",
          "multimedia":"null",
          "seo_name":"Harold-C-Schonberg",
          "sort_name":"Schonberg, Harold C.",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Matt Zoller Seitz",
          "multimedia":"null",
          "seo_name":"Matt-Zoller-Seitz",
          "sort_name":"Seitz, Matt Zoller",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Andre Sennwald",
          "multimedia":"null",
          "seo_name":"Andre-Sennwald",
          "sort_name":"Sennwald, Andre",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Richard F. Shepard",
          "multimedia":"null",
          "seo_name":"Richard-F-Shepard",
          "sort_name":"Shepard, Richard F.",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Harry T. Smith",
          "multimedia":"null",
          "seo_name":"Harry-T-Smith",
          "sort_name":"Smith, Harry T.",
          "status":""
       },
       {
          "bio":"Stephen Holden is a film and music critic for The Times; he joined the culture staff in 1988. Prior to that, he was a pop music critic and journalist for Rolling Stone, The Village Voice, and numerous other magazines and anthologies. Drawing on his experiences as a journalist and record executive, he wrote a satirical novel about the record business, \"Triple Platinum,\"  that was published in 1980 by Dell Books. In 1986, he won a Grammy with six other writers for Best Album Notes for \"The Voice: The Columbia Years, a Frank Sinatra Anthology.\" Born July 18, 1941, Mr. Holden graduated from Yale University in 1963 with a Bachelor of Arts degree in English and was elected Class Poet.",
          "display_name":"Stephen Holden",
          "multimedia":{
             "resource":{
                "credit":"Brent Murray/<br>NYTimes.com",
                "height":163,
                "src":"http://nytimes.com/images/2007/01/05/movies/sholden.163.jpg",
                "type":"image",
                "width":220
             }
          },
          "seo_name":"Stephen-Holden",
          "sort_name":"Stephen Holden",
          "status":"full-time"
       },
       {
          "bio":"",
          "display_name":"Michael Stern",
          "multimedia":"null",
          "seo_name":"Michael-Stern",
          "sort_name":"Stern, Michael",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Dana Stevens",
          "multimedia":"null",
          "seo_name":"Dana-Stevens",
          "sort_name":"Stevens, Dana",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Theodore Strauss",
          "multimedia":"null",
          "seo_name":"Theodore-Strauss",
          "sort_name":"Strauss, Theodore",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Dan Sullivan",
          "multimedia":"null",
          "seo_name":"Dan-Sullivan",
          "sort_name":"Sullivan, Dan",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Howard Thompson",
          "multimedia":"null",
          "seo_name":"Howard-Thompson",
          "sort_name":"Thompson, Howard",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"C. Hooper Trask",
          "multimedia":"null",
          "seo_name":"C-Hooper-Trask",
          "sort_name":"Trask, C. Hooper",
          "status":""
       },
       {
          "bio":"",
          "display_name":"Lawrence Van Gelder",
          "multimedia":"null",
          "seo_name":"Lawrence-Van-Gelder",
          "sort_name":"Van Gelder, Lawrence",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"Andy Webster",
          "multimedia":"null",
          "seo_name":"Andy-Webster",
          "sort_name":"Webster, Andy",
          "status":"part-time"
       },
       {
          "bio":"",
          "display_name":"A. H. Weiler",
          "multimedia":"null",
          "seo_name":"A-H-Weiler",
          "sort_name":"Weiler, A. H.",
          "status":"part-time"
       }
    ],
    "status":"OK"
 }

@responses.activate
def test_all_critics():
    responses.add(responses.GET, URL, json=expected_result, status=200)
    query = get_critics()
    expected = expected_result, expected_result["num_results"]
    assert query == expected
    
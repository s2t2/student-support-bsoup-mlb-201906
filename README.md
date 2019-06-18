
## Process Description

Steps to get stats on a given player:

  + Visit https://www.baseball-reference.com/
  + Find the "View any Active Player" section, choose a team from the dropdown, then choose a player from the dropdown, then click "Go" to be forwarded to a player-specific page, where stats about that player can be found.

## Tech Feasibility Investigation Notes

Inspect the page to find some uniquely-identifying identifiers/ classes / attributes of the elements we care about.

The HTML element for the team dropdown (with abbreviated options) is:

```html
<select name="team_val"
        class="sr_pages_nav no_chosen sr_load_json"
        id="selector_0"
        data-json-key="player_json"
        data-fill="#player_roster .player_list">

    <option value="" selected="selected" disabled="disabled">Choose a Team</option>
	<option value="ARI">Arizona Diamondbacks</option>
	<option value="ATL">Atlanta Braves</option>
	<option value="BAL">Baltimore Orioles</option>
	<option value="BOS">Boston Red Sox</option>
    <option value="CHC">Chicago Cubs</option>
    etc...
	<option value="NYM">New York Mets</option>
    <option value="NYY">New York Yankees</option>
    etc...
	<option value="WSN">Washington Nationals</option>

</select>
```

The HTML element for the team dropdown (with abbreviated options) is:

```html
<select name="1"
        class="sr_pages_nav no_chosen player_list"
        id="selector_0">

    <option disabled="" selected="" value="">Pick a Player</option>
    <option value="/players/a/adamsch01.shtml">Chance Adams</option>
    <option value="/players/a/andujmi01.shtml">Miguel Andujar</option>
    <option value="/players/b/barreja01.shtml">Jake Barrett</option>
    <option value="/players/b/betande01.shtml">Dellin Betances</option>
    <option value="/players/b/birdgr01.shtml">Greg Bird</option>
    <option value="/players/b/brittza01.shtml">Zack Britton</option>
    <option value="/players/c/cessalu01.shtml">Luis Cessa</option>
    etc...
    <option value="/players/v/voitlu01.shtml">Luke Voit</option>
    <option value="/players/w/wadety01.shtml">Tyler Wade</option>

</select>
```

As a future step, we might want to use the Selenium package to automate the process of selecting certain inputs from these dropdowns. But for now let's continue a manual process of gathering the data.

After clicking "Go" we are redirected to a page like https://www.baseball-reference.com/players/c/cessalu01.shtml. There are many data tables on this page, so we need to identify the table(s) we care about, and any identifying attributes of those HTML tables. Here are some of the table containers I see:

```html
<div class="stats_pullout">...</div>

<div id="all_pitching_standard">...</div>

<div id="all_pitching_value">...</div>

etc...
```

Some of these look to be messily formatted as combinations of headers and paragraph tags. But I was able to also find some HTML data `table` elements, which are generally more easy to parse unless there are idiosyncrasies with the way the table is formatted.


```html
<table id="pitching_value" >
    <caption>Player Value--Pitching</caption>

    <thead>
        <tr>
            <th data-stat="year_ID" scope="col">Year</th>
            <th data-stat="age" scope="col" >Age</th>
            <th data-stat="team_ID">Tm</th>
            etc.
        </tr>
   </thead>

   <tbody>
        <tr id="pitching_value.2016" class="full" data-row="0">
            <th scope="row" class="left " data-stat="year_ID">2016</th>
            <td class="right " data-stat="age">24</td>
            <td class="left " data-stat="team_ID">
                <a href="/teams/NYY/2016.shtml" title="New York Yankees">NYY</a>
            </td>
            <td class="left " data-stat="lg_ID">
                <a href="/leagues/AL/2016.shtml">AL</a>
            </td>
            <td class="right " data-stat="IP">70.1</td>
            <td class="right " data-stat="G">17</td>
            <td class="right " data-stat="GS">9</td>
            <td class="right " data-stat="R">36</td>
            <td class="right " data-stat="runs_avg">4.61</td>
            <td class="right " data-stat="opp_runs_avg">4.62</td>
            <td class="right " data-stat="runs_avg_defense">0.01</td>
            <td class="right " data-stat="runs_avg_sprp">0.05</td>
            <td class="right " data-stat="PPF_custom">101.1</td>
            <td class="right " data-stat="runs_avg_avg_pitcher">4.71</td>
            <td class="right iz" data-stat="runs_above_avg_pitch">0</td>
            <td class="right " data-stat="WAA" csk="0.02">0.0</td>
            <td class="right " data-stat="GR_leverage_index_avg">.32</td>
            <td class="right " data-stat="WAA_adj">-0.1</td>
            <td class="right " data-stat="WAR_pitch" csk="0.64">0.6</td>
            <td class="right " data-stat="runs_above_rep_pitch">8</td>
            <td class="right " data-stat="waa_win_perc">.501</td>
            <td class="right " data-stat="waa_win_perc_162">.500</td>
            <td class="right " data-stat="Salary">$507,500</td>
            <td class="left iz" data-stat="award_summary"></td>
        </tr>

        <tr id="pitching_value.2017" class="full" data-row="1">
            <th scope="row" class="left " data-stat="year_ID">2017</th>
            <td class="right " data-stat="age">25</td>
            <td class="left " data-stat="team_ID">
                <a href="/teams/NYY/2017.shtml" title="New York Yankees">NYY</a>
            </td>
            <td class="left " data-stat="lg_ID">
                <a href="/leagues/AL/2017.shtml">AL</a>
            </td>
            <td class="right " data-stat="IP">36.0</td>
            <td class="right " data-stat="G">10</td>
            <td class="right " data-stat="GS">5</td>
            <td class="right " data-stat="R">21</td>
            <td class="right " data-stat="runs_avg">5.25</td>
            <td class="right " data-stat="opp_runs_avg">4.67</td>
            <td class="right " data-stat="runs_avg_defense">0.10</td>
            <td class="right " data-stat="runs_avg_sprp">-0.01</td>
            <td class="right " data-stat="PPF_custom">102.3</td>
            <td class="right " data-stat="runs_avg_avg_pitcher">4.66</td>
            <td class="right " data-stat="runs_above_avg_pitch">-3</td>
            <td class="right " data-stat="WAA" csk="-0.26">-0.3</td>
            <td class="right " data-stat="GR_leverage_index_avg">.41</td>
            <td class="right " data-stat="WAA_adj">0.0</td>
            <td class="right " data-stat="WAR_pitch" csk="0.07">0.1</td>
            <td class="right " data-stat="runs_above_rep_pitch">1</td>
            <td class="right " data-stat="waa_win_perc">.474</td>
            <td class="right " data-stat="waa_win_perc_162">.498</td>
            <td class="right iz" data-stat="Salary"></td>
            <td class="left iz" data-stat="award_summary"></td>
        </tr>

      etc...

   </tbody>

   <tfoot>
       ...
   </tfoot>

</table>
```

So I'll provide an example of how to parse a table like the one above... See section below to set up and run this script.

## Setup

```sh
conda create -n soup-env python=3.7
conda activate soup-env
```

```sh
pip install -r requirements.txt
```

```sh
python get_stats.py
```

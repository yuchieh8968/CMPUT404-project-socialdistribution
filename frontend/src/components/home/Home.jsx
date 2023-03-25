import React, { useEffect, useState } from "react"
import NavBar from "../nav/NavBar";
import './Home.css';

export default function Home() {

    return (
        <div>
            <NavBar />
            <div class="row">
                <div class="column front">
                <h2>Show Friends or Categories.</h2>
                <p>Lorem ipsum dolor sit fasdlkfjhapodfbapsdogipdfgjbnapigtuoeapgiauegpiaurgpierbivpub reairg garepi nerpiubreuoib iugb parubngoureou bo uaboaerubpgriouarepoigjbrepgiobamet, consectetur adipiscing elit.</p>

                </div>
                <div class="column center">
                <h2>Posts Section</h2>
                <p>Lorem ipsum dolor sit fasdlkfjhapodfbapsdogipdfgjbnapigtuoeapgiauegpiaurgpierbivpub reairg garepi nerpiubreuoib iugb parubngoureou bo uaboaerubpgriouarepoigjbrepgiobamet, consectetur adipiscing elit.</p>
                </div>
                <div class="column">
                <h2>Comments Section</h2>
                <p>Lorem ipsum dolor sit fasdlkfjhapodfbapsdogipdfgjbnapigtuoeapgiauegpiaurgpierbivpub reairg garepi nerpiubreuoib iugb parubngoureou bo uaboaerubpgriouarepoigjbrepgiobamet, consectetur adipiscing elit.</p>
                </div>
            </div>
        </div>
    );
}
